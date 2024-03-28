import launch
import pkg_resources

def get_installed_version(package_name):
    """Get the installed version of a package."""
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None

def install_package(package_name, version_spec=None, uninstall_first=False, extra_index_url=None, no_cache_dir=False):
    """Central method to handle package installation with options."""
    package_install_cmd = f"{package_name}{'==' + version_spec if version_spec else ''}"
    options = []
    if extra_index_url:
        options.append(f"--extra-index-url {extra_index_url}")
    if no_cache_dir:
        options.append("--no-cache-dir")
    if uninstall_first and get_installed_version(package_name):
        launch.run(["python", "-m", "pip", "uninstall", "-y", package_name], f"Removing {package_name}")
    options_str = " ".join(options)
    launch.run_pip(f"install {package_install_cmd} {options_str}", package_name, live=True)

def install_dependencies():
    """Install or upgrade required packages with specific dependencies."""
    # Define packages and their dependencies
    dependencies = [
        {"name": "nvidia-cudnn-cu12", "version": "8.9.6.50", "uninstall_first": True, "no_cache_dir": True},
        {"name": "tensorrt", "version": "9.3.0.post12.dev1", "uninstall_first": True, "extra_index_url": "https://pypi.nvidia.com", "no_cache_dir": True},
        {"name": "polygraphy", "extra_index_url": "https://pypi.ngc.nvidia.com", "no_cache_dir": True},
        {"name": "protobuf", "version": "3.20.3", "no_cache_dir": True},
        {"name": "onnx-graphsurgeon", "extra_index_url": "https://pypi.ngc.nvidia.com", "no_cache_dir": True},
        {"name": "optimum", "no_cache_dir": True}
    ]

    for dep in dependencies:
        if not get_installed_version(dep["name"]) or (dep.get("version") and get_installed_version(dep["name"]) != dep["version"]):
            install_package(**dep)

install_dependencies()
