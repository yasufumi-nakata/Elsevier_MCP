from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="elsevier-mcp-server",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="MCP Server for Elsevier Academic APIs (Scopus, SciVal, Abstract Retrieval)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/elsevier-mcp-server",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="elsevier scopus scival academic research mcp cursor ai",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/elsevier-mcp-server/issues",
        "Source": "https://github.com/yourusername/elsevier-mcp-server",
        "Documentation": "https://github.com/yourusername/elsevier-mcp-server#readme",
        "Elsevier Developer": "https://dev.elsevier.com/",
    },
    entry_points={
        "console_scripts": [
            "elsevier-mcp-server=elsevier_mcp_complete:main",
        ],
    },
)