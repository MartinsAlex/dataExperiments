from blocks.customBlocks import Cube

from prefect import flow

@flow(log_prints=True)
def my_flow():
    cube = Cube.load("rubiks-cube")
    print(cube.get_surface_area())

if __name__ == '__main__':
    my_flow()
