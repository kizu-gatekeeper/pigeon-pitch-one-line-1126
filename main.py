"""Entry for make.fun: Pigeon Pitch, One Line.

Writes one city-pigeon startup pitch to entry.txt.

Delivered in the pigeon's own voice, rooftops and all.
"""
import os

LINE = "Coo-op: we already own every rooftop, know every crumb route in the city, and deliver messages no drone can intercept - seed round is just breadcrumbs."
MAX_CHARS = 200


def main():
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds max chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
