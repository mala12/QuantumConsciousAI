from fastapi import APIRouter
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/api/visualization", tags=["visualization"])
def visualization():
    # Example data for visualization
    data = np.random.rand(10, 2)

    # Create a scatter plot
    plt.scatter(data[:, 0], data[:, 1])
    plt.title('Quantum-Consciousness-AI Visualization')
    plt.xlabel('Quantum Dimension')
    plt.ylabel('AI-Consciousness Dimension')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    # Convert image to base64 string for easy transmission
    img_base64 = base64.b64encode(img.read()).decode("utf-8")

    return JSONResponse(content={"visualization": img_base64})

