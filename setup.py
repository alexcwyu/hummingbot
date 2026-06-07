import fnmatch
import os
import subprocess
import sys

import numpy as np
from Cython.Build import cythonize
from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext

is_posix = (os.name == "posix")


class BuildExt(build_ext):
    def build_extensions(self):
        if os.name != "nt" and "-Wstrict-prototypes" in self.compiler.compiler_so:
            self.compiler.compiler_so.remove("-Wstrict-prototypes")
        super().build_extensions()


def main():
    cpu_count = os.cpu_count() or 8
    version = "20260421"
    all_packages = find_packages(where="src", include=["hummingbot", "hummingbot.*"])
    excluded_paths = [
        "hummingbot.connector.gateway.clob_spot.data_sources.injective",
        "hummingbot.connector.gateway.clob_perp.data_sources.injective_perpetual"
    ]
    packages = [
        pkg for pkg in all_packages
        if not any(fnmatch.fnmatch(pkg, pattern) for pattern in excluded_paths)
    ]

    extra_compile_args = []
    extra_link_args = []

    if is_posix:
        os_name = subprocess.check_output("uname").decode("utf8")
        if "Darwin" in os_name:
            extra_compile_args.extend(["-stdlib=libc++", "-std=c++11"])
            extra_link_args.extend(["-stdlib=libc++", "-std=c++11"])
        else:
            extra_compile_args.append("-std=c++11")
            extra_link_args.append("-std=c++11")

    if os.environ.get("WITHOUT_CYTHON_OPTIMIZATIONS"):
        extra_compile_args.append("-O0")

    cython_kwargs = {
        "language": "c++",
        "language_level": 3,
    }

    if is_posix:
        cython_kwargs["nthreads"] = cpu_count

    cython_sources = ["src/hummingbot/**/*.pyx"]

    compiler_directives = {
        "annotation_typing": False,
    }
    if os.environ.get("WITHOUT_CYTHON_OPTIMIZATIONS"):
        compiler_directives.update({
            "optimize.use_switch": False,
            "optimize.unpack_method_calls": False,
        })

    if len(sys.argv) > 1 and sys.argv[1] == "build_ext" and is_posix:
        sys.argv.append(f"--parallel={cpu_count}")

    extensions = cythonize(
        cython_sources,
        compiler_directives=compiler_directives,
        **cython_kwargs
    )

    for ext in extensions:
        ext.extra_compile_args = extra_compile_args
        ext.extra_link_args = extra_link_args
        # Add src/ to include dirs so C++ headers referenced as
        # "hummingbot/core/cpp/..." can be found
        ext.include_dirs.append("src")
        # Fix C++ source file paths: cythonize picks up paths like
        # "hummingbot/core/cpp/X.cpp" from .pyx declarations, but
        # the actual files live under "src/hummingbot/core/cpp/X.cpp"
        ext.sources = [
            os.path.join("src", s) if (
                s.startswith("hummingbot/") and not os.path.exists(s)
                and os.path.exists(os.path.join("src", s))
            ) else s
            for s in ext.sources
        ]

    setup(
        name="hummingbot",
        version=version,
        description="Hummingbot",
        url="https://github.com/hummingbot/hummingbot",
        author="Hummingbot Foundation",
        author_email="dev@hummingbot.org",
        license="Apache 2.0",
        python_requires=">=3.10.12",
        packages=packages,
        package_dir={"": "src"},
        ext_modules=extensions,
        include_dirs=[
            np.get_include(),
            "src",
        ],
        cmdclass={"build_ext": BuildExt},
    )


if __name__ == "__main__":
    main()
