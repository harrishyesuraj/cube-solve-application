# ================================
# 1. IMPORTS
# ================================
import kociemba
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ================================
# 2. APP SETUP
# ================================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================
# 3. INPUT MODEL
# ================================
class CubeInput(BaseModel):
    faces: dict

# ================================
# 4. COLOR MAPPING
# ================================
color_map = {
    "W": "U",
    "R": "R",
    "G": "F",
    "Y": "D",
    "O": "L",
    "B": "B"
}

# ================================
# 5. CONVERT MATRIX → STRING
# ================================
def convert_to_string(faces):
    order = ['U','R','F','D','L','B']
    cube_string = ""

    for face in order:
        if face not in faces:
            raise ValueError(f"Missing face: {face}")

        for row in faces[face]:
            if len(row) != 3:
                raise ValueError(f"Invalid row size in face {face}")

            for col in row:
                if col not in color_map:
                    raise ValueError(f"Invalid color: {col}")

                cube_string += color_map[col]

    return cube_string

# ================================
# 6. ROOT API
# ================================
@app.get("/")
def home():
    return {"status": "API running"}

# ================================
# 7. SOLVE API (FULLY SAFE)
# ================================
@app.post("/solve")
def solve_cube(data: CubeInput):
    try:
        faces = data.faces

        # ✅ Convert input
        cube_string = convert_to_string(faces)

        print("Cube string:", cube_string)

        # ✅ Check length
        if len(cube_string) != 54:
            return {
                "solution": [],
                "error": "Invalid cube length"
            }

        # ✅ Check color count (must be exactly 9 each)
        for c in "URFDLB":
            if cube_string.count(c) != 9:
                return {
                    "solution": [],
                    "error": f"Invalid color count for {c}"
                }

        # ✅ Solved cube check
        solved = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        if cube_string == solved:
            print("[Solver] Cube is already solved.")
            return {"solution": []}

        # ✅ Solve cube safely
        solution = kociemba.solve(cube_string)

        return {
            "solution": solution.split()
        }

    except Exception as e:
        print("ERROR:", e)

        return {
            "solution": [],
            "error": "Invalid cube or unsolvable configuration"
        }
