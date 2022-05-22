if __name__ == "__main__":

    import os
    import sys
    import shutil

    glb_path = sys.argv[1]
    files = [os.path.relpath(os.path.join(root, file), glb_path) for root, _, files in os.walk(
        glb_path) for file in files if file.endswith(".html")]
    for rel_path in files:
        path, file = os.path.split(rel_path)
        test_path = os.path.join(glb_path, "template", path)
        if not os.path.exists(test_path):
            os.makedirs(test_path)
        shutil.copyfile(os.path.join(glb_path,rel_path), os.path.join(test_path, file))