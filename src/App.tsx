import { useEffect, useState } from "react";
import { invoke } from "@tauri-apps/api/core";
import "./App.css";

type AppInfo = {
  appName: string;
  version: string;
  coreStatus: string;
  operatingMode: string;
};

type ViewState =
  { status: "loading" } | { status: "ready"; data: AppInfo } | { status: "error"; message: string };

function readableError(error: unknown): string {
  if (error instanceof Error) return error.message;
  if (typeof error === "string") return error;
  return "The application core returned an unreadable error.";
}

function App() {
  const [state, setState] = useState<ViewState>({ status: "loading" });

  useEffect(() => {
    let active = true;

    invoke<AppInfo>("get_app_info")
      .then((data) => {
        if (active) setState({ status: "ready", data });
      })
      .catch((error: unknown) => {
        if (active) {
          setState({ status: "error", message: readableError(error) });
        }
      });

    return () => {
      active = false;
    };
  }, []);

  return (
    <main className="app-shell">
      <section className="app-card" aria-live="polite">
        <p className="eyebrow">Project foundation</p>
        <h1>Project Integrity OS</h1>

        {state.status === "loading" && <p>Loading core information...</p>}

        {state.status === "error" && (
          <div className="error-panel" role="alert">
            <strong>Core unavailable</strong>
            <p>{state.message}</p>
          </div>
        )}

        {state.status === "ready" && (
          <dl className="info-grid">
            <div>
              <dt>Application</dt>
              <dd>{state.data.appName}</dd>
            </div>
            <div>
              <dt>Version</dt>
              <dd>{state.data.version}</dd>
            </div>
            <div>
              <dt>Core status</dt>
              <dd>{state.data.coreStatus}</dd>
            </div>
            <div>
              <dt>Operating mode</dt>
              <dd>{state.data.operatingMode}</dd>
            </div>
          </dl>
        )}
      </section>
    </main>
  );
}

export default App;
