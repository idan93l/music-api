from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Music API")
DEFAULT_BPM = int(os.getenv("DEFAULT_BPM", "120"))
SECRET_TOKEN = os.getenv("SECRET_TOKEN", "not-set")

# -----------------------------
# Music theory data
# -----------------------------

SEMITONE_MAP_SHARP = ["C", "C#", "D", "D#", "E", "F",
                      "F#", "G", "G#", "A", "A#", "B"]

SEMITONE_MAP_FLAT  = ["C", "Db", "D", "Eb", "E", "F",
                      "Gb", "G", "Ab", "A", "Bb", "B"]

NOTE_TO_INDEX = {
    "C": 0, "B#": 0,
    "C#": 1, "Db": 1,
    "D": 2,
    "D#": 3, "Eb": 3,
    "E": 4, "Fb": 4,
    "F": 5, "E#": 5,
    "F#": 6, "Gb": 6,
    "G": 7,
    "G#": 8, "Ab": 8,
    "A": 9,
    "A#": 10, "Bb": 10,
    "B": 11, "Cb": 11,
}

FLAT_KEYS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]

CHORD_TYPES = {
    "maj":   [0, 4, 7],
    "min":   [0, 3, 7],
    "dim":   [0, 3, 6],
    "aug":   [0, 4, 8],
    "sus2":  [0, 2, 7],
    "sus4":  [0, 5, 7],
    "7":     [0, 4, 7, 10],
    "maj7":  [0, 4, 7, 11],
    "min7":  [0, 3, 7, 10],
    "dim7":  [0, 3, 6, 9],
    "m7b5":  [0, 3, 6, 10],
    "6":     [0, 4, 7, 9],
    "m6":    [0, 3, 7, 9],
    "add9":  [0, 4, 7, 14],
    "madd9": [0, 3, 7, 14],
}

SCALE_PATTERNS = {
    "Major (Ionian)":        [0, 2, 4, 5, 7, 9, 11],
    "Dorian":               [0, 2, 3, 5, 7, 9, 10],
    "Phrygian":             [0, 1, 3, 5, 7, 8, 10],
    "Lydian":               [0, 2, 4, 6, 7, 9, 11],
    "Mixolydian":           [0, 2, 4, 5, 7, 9, 10],
    "Aeolian (Natural Min)": [0, 2, 3, 5, 7, 8, 10],
    "Locrian":              [0, 1, 3, 5, 6, 8, 10],
    "Harmonic Minor":       [0, 2, 3, 5, 7, 8, 11],
    "Melodic Minor (Asc.)": [0, 2, 3, 5, 7, 9, 11],
    "Major Pentatonic":     [0, 2, 4, 7, 9],
    "Minor Pentatonic":     [0, 3, 5, 7, 10],
    "Blues":                [0, 3, 5, 6, 7, 10],
}

PROGRESSIONS = [
    ["I", "V", "vi", "IV"],
    ["ii", "V", "I"],
    ["I", "vi", "IV", "V"],
    ["I", "IV", "V", "IV"],
    ["vi", "IV", "I", "V"],
]

ROMAN_TO_DEGREE = {
    "I": 1, "ii": 2, "iii": 3, "IV": 4, "V": 5, "vi": 6, "vii°": 7,
}

def pick_note_names(root: str, intervals):
    root_index = NOTE_TO_INDEX[root]
    use_flat = ("b" in root) or (root in FLAT_KEYS)
    semitone_map = SEMITONE_MAP_FLAT if use_flat else SEMITONE_MAP_SHARP

    notes = []
    for interval in intervals:
        idx = (root_index + interval) % 12
        notes.append(semitone_map[idx])
    return notes

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def hello():
    return f"🎶 This is {APP_NAME}, Ready to Rock? 🎸"

@app.route("/beat")
def beat():
    bpm_choices = [80, 90, 100, 110, 120, 130, 140, DEFAULT_BPM]
    bpm = random.choice(bpm_choices)
    length = random.randint(8, 16)
    hit_probability = random.choice([0.4, 0.5, 0.6, 0.7])

    pattern = [
        1 if random.random() < hit_probability else 0
        for _ in range(length)
    ]

    return jsonify({
        "bpm": bpm,
        "steps": length,
        "hit_probability": hit_probability,
        "pattern": pattern,
    })

@app.route("/chord")
def chord():
    root = random.choice(list(NOTE_TO_INDEX.keys()))
    chord_type, intervals = random.choice(list(CHORD_TYPES.items()))
    notes = pick_note_names(root, intervals)

    return jsonify({
        "root": root,
        "type": chord_type,
        "intervals_semitones": intervals,
        "notes": notes,
    })

@app.route("/scale")
def scale():
    root = random.choice(list(NOTE_TO_INDEX.keys()))
    scale_name, intervals = random.choice(list(SCALE_PATTERNS.items()))
    notes = pick_note_names(root, intervals)

    return jsonify({
        "root": root,
        "scale": scale_name,
        "intervals_semitones": intervals,
        "notes": notes,
    })

@app.route("/progression")
def progression():
    major_roots = ["C", "G", "D", "A", "E", "B", "F", "Bb", "Eb", "Ab", "Db", "Gb"]
    key_root = random.choice(major_roots)
    progression = random.choice(PROGRESSIONS)

    degree_to_type = {1: "maj", 2: "min", 3: "min", 4: "maj", 5: "maj", 6: "min", 7: "dim"}

    chords = []
    for symbol in progression:
        degree = ROMAN_TO_DEGREE.get(symbol.replace("°", ""), 1)
        chord_type = degree_to_type.get(degree, "maj")

        major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]
        key_index = NOTE_TO_INDEX[key_root]
        degree_interval = major_scale_intervals[degree - 1]

        use_flat = ("b" in key_root) or (key_root in FLAT_KEYS)
        semitone_map = SEMITONE_MAP_FLAT if use_flat else SEMITONE_MAP_SHARP
        chord_root = semitone_map[(key_index + degree_interval) % 12]

        chords.append({
            "roman": symbol,
            "root": chord_root,
            "type": chord_type,
            "notes": pick_note_names(chord_root, CHORD_TYPES[chord_type]),
        })

    return jsonify({
        "key": key_root,
        "scale": "Major",
        "progression": progression,
        "chords": chords,
    })

# ✅ Kubernetes health endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/config")
def config():
    return jsonify({
        "app_name": APP_NAME,
        "default_bpm": DEFAULT_BPM,
        "secret_token_set": SECRET_TOKEN != "not-set"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
