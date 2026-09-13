from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated system database
SYSTEM_DATA = {
    "status": "ONLINE",
    "clearance_level": 3,
    "system_memory": "82% allocated",
    "active_agents": ["Ghost", "Viper", "Cipher"],
    "classified_files": {
        "file_01": "Operation Blackout: Target mainframe secured at 0200 hours.",
        "file_02": "AI Core Metrics: Neural link stability dropping. Caution advised.",
        "file_03": "Encrypted Payload: 0x4A892F110B (Decryption key required)"
    }
}

# Interactive Cyberpunk UI Terminal Homepage
@app.route("/")
def terminal_ui():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CYBER_OS // TERMINAL</title>
        <style>
            body { background-color: #0d0221; color: #00ffcc; font-family: 'Courier New', monospace; padding: 30px; }
            h1 { color: #ff0055; text-shadow: 0 0 8px #ff0055; }
            .box { border: 2px solid #00ffcc; padding: 20px; box-shadow: 0 0 15px #00ffcc; max-width: 650px; background: #050014; }
            a { color: #ff0055; text-decoration: none; font-weight: bold; }
            a:hover { text-decoration: underline; color: #00ffcc; }
            .cmd { color: #ffe600; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>> CYBER_OS v4.09 INITIALIZED</h1>
            <p>Welcome, Operator. Select a command endpoint to execute:</p>
            <ul>
                <li><span class="cmd">SYSTEM STATUS:</span> <a href="/api/status" target="_blank">/api/status</a></li>
                <li><span class="cmd">ACTIVE AGENTS:</span> <a href="/api/agents" target="_blank">/api/agents</a></li>
                <li><span class="cmd">READ FILE 1:</span> <a href="/api/files/file_01" target="_blank">/api/files/file_01</a></li>
                <li><span class="cmd">READ FILE 2:</span> <a href="/api/files/file_02" target="_blank">/api/files/file_02</a></li>
            </ul>
            <p><i>Tip: Use parameters like <code>/api/execute?command=override</code> to trigger system events.</i></p>
        </div>
    </body>
    </html>
    """
    return html_content

# API Endpoint: System Diagnostics
@app.route("/api/status")
def get_status():
    return jsonify({
        "node": "SECTOR-7G",
        "system_status": SYSTEM_DATA["status"],
        "clearance": SYSTEM_DATA["clearance level"],
        "memory_load": SYSTEM_DATA["system memory"]
    })

# API Endpoint: Get Agents
@app.route("/api/agents")
def get_agents():
    return jsonify({
        "agent_count": len(SYSTEM_DATA["active_agents"]),
        "agents": SYSTEM_DATA["active_agents"]
    })

# Dynamic Route: Fetch Classified Files
@app.route("/api/files/<file_id>")
def get_file(file_id):
    content = SYSTEM_DATA["classified_files"].get(file_id)
    if content:
        return jsonify({"file_id": file_id, "content": content, "status": "DECRYPTED"}), 200
    return jsonify({"error": "ACCESS DENIED / FILE NOT FOUND"}), 404

# Dynamic Command Execution via Query Parameter
@app.route("/api/execute")
def execute_command():
    cmd = request.args.get("command", "").lower()
    
    if cmd == "override":
        return jsonify({"result": "SYSTEM OVERRIDE SUCCESSFUL", "clearance": "MAXIMUM"})
    elif cmd == "reboot":
        return jsonify({"result": "REBOOT SEQUENCE INITIATED... Connection lost."})
    else:
        return jsonify({
            "error": "UNKNOWN COMMAND",
            "usage": "Try /api/execute?command=override or /api/execute?command=reboot"
        }), 400

if __name__ == "__main__":
    app.run(debug=True)