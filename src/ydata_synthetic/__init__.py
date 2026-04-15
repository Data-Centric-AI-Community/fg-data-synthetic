#from .version import __version__

warn(
    """
    `import ydata_synthetic` is deprecated and will not receive more updates. 
    Please install fg-data-synthetic via `pip install fg-data-synthetic` and use `import data_synthetic` instead.
    """,
    DeprecationWarning,
    stacklevel=2,
)
