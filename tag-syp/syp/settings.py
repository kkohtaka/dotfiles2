REQUIREMENTS_ROOT_DIR = "~/dotfiles/syp/"

REQUIREMENTS_FILES['apt-repository'] = {
    "file": "apt-repository.txt",
    "pacman": "apt-add-repository",
    "install": "--update",
    "uninstall": "--remove",
}

REQUIREMENTS_FILES['apm'] = {
    "file": "apm.txt",
    "pacman": "apm",
    "install": "install",
    "uninstall": "uninstall",
}
