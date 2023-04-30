def run(src, filename = 'editor'):
    ns = {'__name__':'__main__', '__file__': filename}
    state = 1
    try:
        exec(src, ns)
    except Exception as exc:
        print(f"Error: {src}, at: {ns}")
        state = 0
    return state