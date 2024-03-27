import launch
import sys

python = sys.executable


def install():
    if not launch.is_installed("importlib_metadata"):
        launch.run_pip("install importlib_metadata", "importlib_metadata", live=True)
    from importlib_metadata import version

    if launch.is_installed("tensorrt"):
        if not version("tensorrt") == "9.3.0.post12.dev1":
            launch.run(
                ["python", "-m", "pip", "uninstall", "-y", "tensorrt"],
                "removing old version of tensorrt",
            )

    if not launch.is_installed("tensorrt"):
        print("TensorRT is not installed! Installing...")
        launch.run_pip(
            "install nvidia-cudnn-cu12==8.9.6.50 --no-cache-dir", "nvidia-cudnn-cu12"
        )
        launch.run_pip(
            "install --pre --extra-index-url https://pypi.nvidia.com tensorrt==9.3.0.post12.dev1 --no-cache-dir",
            "tensorrt",
            live=True,
        )
        launch.run(
            ["python", "-m", "pip", "uninstall", "-y", "nvidia-cudnn-cu12"],
            "removing nvidia-cudnn-cu12",
        )

    if launch.is_installed("nvidia-cudnn-cu12"):
        if version("nvidia-cudnn-cu12") == "8.9.6.50":
            launch.run(
                ["python", "-m", "pip", "uninstall", "-y", "nvidia-cudnn-cu12"],
                "removing nvidia-cudnn-cu12",
            )

    # Polygraphy
    if not launch.is_installed("polygraphy"):
        print("Polygraphy is not installed! Installing...")
        launch.run_pip(
            "install polygraphy --extra-index-url https://pypi.ngc.nvidia.com",
            "polygraphy",
            live=True,
        )

    # ONNX GS
    if not launch.is_installed("onnx_graphsurgeon"):
        print("GS is not installed! Installing...")
        launch.run_pip("install protobuf==3.20.2", "protobuf", live=True)
        launch.run_pip(
            "install onnx-graphsurgeon --extra-index-url https://pypi.ngc.nvidia.com",
            "onnx-graphsurgeon",
            live=True,
        )

    # OPTIMUM
    if not launch.is_installed("optimum"):
        print("Optimum is not installed! Installing...")
        launch.run_pip(
            "install optimum",
            "optimum",
            live=True,
        )


install()
