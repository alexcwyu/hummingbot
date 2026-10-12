#!/usr/bin/env python
"""Compatibility launcher for source checkouts and existing Docker commands."""
import path_util  # noqa: F401

from hummingbot.client.interactive import *  # noqa: F401,F403
from hummingbot.client.interactive import main


if __name__ == "__main__":
    main()
