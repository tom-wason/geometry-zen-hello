# webgl.py
from ga import *
# We will control the horizontal. We will control the vertical.
from browser import *

# Discard any old canvas if it exists. 
canvas = document.getElementById("canvas")
if (canvas):
    canvas.parentNode.removeChild(canvas)

container = document.createElement("div")
document.body.appendChild(container)

scene = Scene()

# Aspect ratio will be reset in onWindowResize
camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()

view = document.getElementById("view")
view.parentNode.insertBefore(renderer.domElement, view)

geometry = CubeGeometry(1, 1, 1)
geometry = SphereGeometry(1.0, 32, 24)
material = MeshNormalMaterial()
mesh = Mesh(geometry, material)
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000 # run for 10 seconds
startTime =  None

def render():
    mesh.rotation.x = mesh.rotation.x + 0.02
    mesh.rotation.y = mesh.rotation.y + 0.02
    mesh.rotation.z = mesh.rotation.z + 0.02
        
    renderer.render(scene, camera)

def onWindowResize():
    # TODO: width / height => window.innerSize.aspectRatio
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    # TODO: renderer.size = window.innerSize
    renderer.size = (window.innerWidth, window.innerHeight)
    
def step(timestamp):
    global requestID, progress, startTime
    if (startTime):
        progress = timestamp - startTime
    else:
        if (timestamp):
            startTime = timestamp
        else:
            progress = 0
        
    if (progress < progressEnd):
        requestID = window.requestAnimationFrame(step)
        render()
    else:
        window.cancelAnimationFrame(requestID)
        view.parentNode.removeChild(renderer.domElement)
        # TODO: Remove the "resize" event listener

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)