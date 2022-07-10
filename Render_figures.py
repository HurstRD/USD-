def render_figures(code, code_path, output_dir, output_base, context,
                   function_name, config, context_reset=False,
                   close_figs=False,
                   code_includes=None):
    """
    Run a pyplot script and save the images in *output_dir*.

    Save the images under *output_dir* with file names derived from
    *output_base*
    """
    formats = get_plot_formats(config)


    # Try to determine if all images already exist


    is_doctest, code_pieces = _split_code_at_show(code)


    # Look for single-figure output files first
    all_exists = True
    img = ImageFile(output_base, output_dir)
    for format, dpi in formats:
        if context or out_of_date(code_path, img.filename(format),
                                  includes=code_includes):
            all_exists = False
            break
        img.formats.append(format)


    if all_exists:
        return [(code, [img])]


    # Then look for multi-figure output files
    results = []
    all_exists = True
    for i, code_piece in enumerate(code_pieces):
        images = []
        for j in itertools.count():
            if len(code_pieces) > 1:
                img = ImageFile('%s_%02d_%02d' % (output_base, i, j),
                                output_dir)
            else:
                img = ImageFile('%s_%02d' % (output_base, j), output_dir)
            for fmt, dpi in formats:
                if context or out_of_date(code_path, img.filename(fmt),
                                          includes=code_includes):
                    all_exists = False
                    break
                img.formats.append(fmt)


            # assume that if we have one, we have them all
            if not all_exists:
                all_exists = (j > 0)
                break
            images.append(img)
        if not all_exists:
            break
        results.append((code_piece, images))


    if all_exists:
        return results


    # We didn't find the files, so build them


    results = []
    ns = plot_context if context else {}


    if context_reset:
        clear_state(config.plot_rcparams)
        plot_context.clear()


    close_figs = not context or close_figs


    for i, code_piece in enumerate(code_pieces):


        if not context or config.plot_apply_rcparams:
            clear_state(config.plot_rcparams, close_figs)
        elif close_figs:
            plt.close('all')


        _run_code(doctest.script_from_examples(code_piece) if is_doctest
                  else code_piece,
                  code_path, ns, function_name)


        images = []
        fig_managers = _pylab_helpers.Gcf.get_all_fig_managers()
        for j, figman in enumerate(fig_managers):
            if len(fig_managers) == 1 and len(code_pieces) == 1:
                img = ImageFile(output_base, output_dir)
            elif len(code_pieces) == 1:
                img = ImageFile("%s_%02d" % (output_base, j), output_dir)
            else:
                img = ImageFile("%s_%02d_%02d" % (output_base, i, j),
                                output_dir)
            images.append(img)
            for fmt, dpi in formats:
                try:
                    figman.canvas.figure.savefig(img.filename(fmt), dpi=dpi)
                except Exception as err:
                    raise PlotError(traceback.format_exc()) from err
                img.formats.append(fmt)


        results.append((code_piece, images))


    if not context or config.plot_apply_rcparams:
        clear_state(config.plot_rcparams, close=not context)


    return results
