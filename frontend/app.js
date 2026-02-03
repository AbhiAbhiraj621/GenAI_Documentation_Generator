import { useState } from "react";

function App() {
  const [code, setCode] = useState("");
  const [docType, setDocType] = useState("technical");
  const [result, setResult] = useState("");

  const generateDoc = async () => {
    try {
      setResult("Processing... please wait.");

      const response = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          pipeline_code: code,
          doc_type: docType,
        }),
      });

      const data = await response.json();
      setResult(data.documentation);
    } catch (err) {
      console.error("API error", err);
      setResult("Error generating documentation.");
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>GenAI ETL Documentation</h2>

      <textarea
        rows="10"
        cols="70"
        placeholder="Paste ETL code or config..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <br /><br />

      <select value={docType} onChange={(e) => setDocType(e.target.value)}>
        <option value="technical">Technical Documentation</option>
        <option value="business">Business Summary</option>
      </select>

      <br /><br />

      <button onClick={generateDoc}>Generate Documentation</button>

      <hr />

      <h3>Output</h3>
      <pre style={{ whiteSpace: "pre-wrap" }}>{result}</pre>
    </div>
  );
}

export default App;
