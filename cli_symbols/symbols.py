# cli_symbols.py

# Setup / Progress
BOX = "📦 "
HOURGLASS = "⏳ "
REFRESH = "🔄 "
WRENCH = "🔧 "
GEAR = "⚙️ "

# Success / Error / Warning
CHECK = "✅ "
CROSS = "❌ "
WARNING = "⚠️ "
STOP = "🛑 "
BOXED_CHECK = "☑️ "

# Performance / Benchmark
ROCKET = "🚀 "
CHART = "📊 "
STOPWATCH = "⏱ "
FIRE = "🔥 "

# File / Data
FOLDER = "📂 "
FILE = "📄 "
ARCHIVE = "🗃 "
BRAIN = "🧠 "

# AI / ML / Inference
BOT = "🤖 "
EXPERIMENT = "🧪 "
SATELLITE = "🛰 "
THREAD = "🧵 "

# CLI / Logging
SPEAKER = "📢 "
NOTE = "📝 "
BALLOON = "💬 "
KEYBOARD = "⌨️ "

# Optional: helper log function
def log(msg: str, icon: str = NOTE):
    print(f"{icon} {msg}")

# Usage examples:
if __name__ == "__main__":
	print(f"{BOX} Downloading model...")
	print(f"{CHECK} Model loaded successfully.")
	print(f"{ROCKET} Running benchmark...")
	print(f"{FIRE} Tokens/sec: 4200")
	print(f"{CROSS} Error: model path not found.")

	log("Starting inference server...", SPEAKER)
	log("Prompt received.", BALLOON)

