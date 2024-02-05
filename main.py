import curses
import json
import os
import sys


def load_items_from_json_file(file_path: str):
    items = None

    with open(file_path) as file:
        loaded_json = json.load(file)
        items = loaded_json["items"]
    
    return items


def display_items(stdscr, items, selecting_index):
    stdscr.addstr(0, 0, "press char or UP/DOWN to select")

    for idx, item in enumerate(items):
        text = "{}: {}".format(item["key"], item["name"])
        attr = None

        if idx == selecting_index:
            attr = curses.A_REVERSE
        else:
            attr = curses.A_NORMAL

        stdscr.addstr(idx+1, 0, text, attr)


# returns: (
#   idx (-1 if not found): int,
#   has_bindings: bool,
#   has_command: bool
# )
def get_next_items_state(items, key):
    for idx, item in enumerate(items):
        if item["key"] == key:
            return (
                idx,
                "bindings" in item.keys(),
                "command" in item.keys()
            )

    return (-1, False, False)


def main(stdscr):
    global command

    home_path = os.path.expanduser("~")
    config_path = os.path.join(home_path, ".wkshell_config.json")
    items = load_items_from_json_file(config_path)

    selecting_index = 0

    while True:
        stdscr.clear()
        display_items(stdscr, items, selecting_index)

        keycode = stdscr.getch()
        if keycode < 0:
            continue

        # move selecting cursor
        if keycode == curses.KEY_UP:
            selecting_index = max(0, selecting_index - 1)
        elif keycode == curses.KEY_DOWN:
            selecting_index = min(len(items) - 1, selecting_index + 1)

        # process Enter key
        if keycode == 10:
            keycode = ord(items[selecting_index]["key"])
        # process Esc key
        if keycode == 27:
            stdscr.nodelay(True)
            if stdscr.getch() == -1:
                exit(1)
            stdscr.nodelay(False)

        # update items / decide command
        next_idx, has_bnd, has_cmd = get_next_items_state(items, chr(keycode))
        if has_bnd:
            items = items[next_idx]["bindings"]
        elif has_cmd:
            command = items[next_idx]["command"]
            break


os.environ.setdefault('ESCDELAY', '25')

command = ""
curses.wrapper(main)
print(command)
print(command, file=sys.stderr)
