def calculate_rms(expected_image, actual_image):
    """
    Calculate the per-pixel errors, then compute the root mean square error.
    """
    if expected_image.shape != actual_image.shape:
        raise ImageComparisonFailure(
            "Image sizes do not match expected size: {} "
            "actual size {}".format(expected_image.shape, actual_image.shape))
    # Convert to float to avoid overflowing finite integer types.
    return np.sqrt(((expected_image - actual_image).astype(float) ** 2).mean())
