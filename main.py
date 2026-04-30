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

        if len(faces[face]) != 3:
            raise ValueError(f"Face {face} must have 3 rows")

        for row in faces[face]:
            if len(row) != 3:
                raise ValueError(f"Each row in face {face} must have 3 elements")

            for col in row:
                if col not in color_map:
                    raise ValueError(f"Invalid color detected: {col}")

                cube_string += color_map[col]

    return cube_string

# ================================
# 6. ROOT API
# ================================
@app.get("/")
def home():
    return {"status": "API running"}

# ================================
# 7. VALIDATION FUNCTION
# ================================
def validate_cube(cube_string):
    if len(cube_string) != 54:
        return False, "Cube string must be 54 characters"

    for c in "URFDLB":
        if cube_string.count(c) != 9:
            return False, f"Invalid count for {c}"

    return True, None

# ================================
# 8. SOLVE API
# ================================
@app.post("/solve")
def solve_cube(data: CubeInput):
    try:
        faces = data.faces

        # Convert faces → cube string
        cube_string = convert_to_string(faces)

        print("🧊 Cube string:", cube_string)

        # Validate cube
        is_valid, error_msg = validate_cube(cube_string)
        if not is_valid:
            return {
                "solution": [],
                "error": error_msg,
                "cube_string": cube_string
            }

        # Solved cube check
        solved = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        if cube_string == solved:
            print("[Solver] Cube is already solved.")
            return {
                "solution": [],
                "message": "Cube already solved"
            }

        # Solve cube
        solution = kociemba.solve(cube_string)

        return {
            "solution": solution.split(),
            "cube_string": cube_string
        }

    except Exception as e:
        print("❌ ERROR:", e)

        return {
            "solution": [],
            "error": str(e),
            "message": "Invalid cube or unsolvable configuration"
        }
