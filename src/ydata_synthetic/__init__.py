from warnings import warn

warn(
    """
    `import ydata_synthetic` is deprecated and will not receive more updates. 
    Please use `import data_synthetic` instead.
    """,
    DeprecationWarning,
    stacklevel=2,
)