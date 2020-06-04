import sys

from PyQt5.QtWidgets import QApplication

from Camera import Camera
from Geo.Material import Material
from Geo.Plane import Plane
from Geo.Sphere import Sphere
from Geo.Vector import Vector
from Light import DiskLight
from RenderWindow import RenderWindow
from Scene import Scene


def main():
    renderApp = QApplication(sys.argv)
    renderView = RenderWindow()

    redLambert = Material(diffuseColor=Vector(0.9, 0.1, 0.1))
    blueLambert = Material(diffuseColor=Vector(0, 0, 0.9))
    greenLambert = Material(diffuseColor=Vector(0.1, 0.9, 0.1))
    whiteLambert = Material(diffuseColor=Vector(0.9, 0.9, 0.9))
    yellowLambert = Material(diffuseColor=Vector(0.95, 0.4, 0.0))
    lightBlueLambert = Material(diffuseColor=Vector(0.1, 0.5, 0.9))
    mirror = Material(reflectionColor=Vector(1, 1, 1), reflectionWeight=1)
    redMirror = Material(reflectionColor=Vector(0.9, 0, 0), reflectionWeight=1)
    emissive = Material(emissionAmount=500)
    glass = Material(refractionWeight=1, reflectionWeight=1)

    sphere02 = Sphere(Vector(10, -20, -146), 30, material=mirror)
    sphere03 = Sphere(Vector(-25, -35, -115), 15, material=redMirror)
    sphere04 = Sphere(Vector(25, -35, -100), 15, material=glass)

    plane01 = Plane(Vector(0, -50, -136), Vector(0, 1, 0), material=whiteLambert)  # bottom wall
    plane02 = Plane(Vector(-50, 0, -136), Vector(1, 0, 0), material=yellowLambert)  # left wall
    plane03 = Plane(Vector(0, 0, -186), Vector(0, 0, 1), material=whiteLambert)  # back wall
    plane04 = Plane(Vector(50, 0, -136), Vector(-1, 0, 0), material=lightBlueLambert)  # right wall
    plane05 = Plane(Vector(0, 50, -136), Vector(0, -1, 0), material=emissive)  # top wall

    light01 = DiskLight(Vector(0, 48, -136), 30, normal=Vector(0, -1, 0), samples=1, isDoubleSided=True, visible=True)

    newScene = Scene(
        {"geometry": [plane01, plane02, plane03, plane04, plane05, sphere02, sphere03, sphere04], "light": [light01]})

    teleCam = Camera(Vector(0, 0, 130), Vector(0, 0, 1), 80, aperture=1.4, focusDist=243, filmFit="Horizontal")
    renderView.startRender(newScene, teleCam)

    sys.exit(renderApp.exec_())


if __name__ == "__main__":
    main()
