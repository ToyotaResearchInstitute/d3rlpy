from setuptools import setup, find_packages


setup(name="d3rlpy",
      version="0.1",
      description="Data-driven Deep Reinforcement Learning Library as an Out-of-the-box Tool",
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      url="https://github.com/takuseno/d3rlpy",
      author="Takuma Seno",
      author_email="takuma.seno@gmail.com",
      license="MIT License",
      install_requires=["torch",
                        "scikit-learn",
                        "tensorboardX",
                        "tqdm",
                        "GPUtil",
                        "h5py",
                        "gym",
                        "kornia"],
      packages=["d3rlpy",
                "d3rlpy.algos",
                "d3rlpy.algos.torch",
                "d3rlpy.dynamics",
                "d3rlpy.dynamics.torch",
                "d3rlpy.metrics",
                "d3rlpy.models",
                "d3rlpy.models.torch",
                "d3rlpy.preprocessing",
                "d3rlpy.experimental",
                "d3rlpy.experimental.server",
                "d3rlpy.online"],
      python_requires=">=3.5.0")
