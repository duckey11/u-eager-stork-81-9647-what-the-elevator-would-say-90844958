"""Entry for the "What the Elevator Would Say" bounty.

The joke: an elevator greets its passenger by name and floor, then
casually reveals it has been keeping track of him. He keeps pressing
9, yet he keeps visiting 14B, and it has watched this for six months.
The last line flips the whole ride from a routine floor announcement
into a quiet blackmail note: his wife thinks he works late. The lift
is not just a machine here, it is a witness that remembers every
button press, and it has finally decided to say so.
"""

ENTRY = "Floor 12, Mr. Chen. You pressed 9 again. I've logged every trip to 14B for six months. Your wife thinks you work late."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
