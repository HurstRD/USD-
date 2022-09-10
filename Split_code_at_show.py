@_api.deprecated("3.5")
def split_code_at_show(text):
    """Split code at plt.show()."""
    return _split_code_at_show(text)[1]
