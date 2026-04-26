import kociemba
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CubeInput(BaseModel):
    faces: dict

color_map = {
    "W": "U",
    "R": "R",
    "G": "F",
    "Y": "D",
    "O": "L",
    "B": "B"
}

def convert_to_string(faces):
    order = ['U','R','F','D','L','B']
    cube_string = ""

    for face in order:
        for row in faces[face]:
            for col in row:
                cube_string += color_map[col]

    return cube_string

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/solve")
def solve_cube(data: CubeInput):
    cube_string = convert_to_string(data.faces)
    solution = kociemba.solve(cube_string)

    return {
        "solution": solution.split()
    }
