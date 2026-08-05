#[derive(serde::Serialize)]
#[serde(rename_all = "camelCase")]
pub struct AppInfo {
    app_name: &'static str,
    version: &'static str,
    core_status: &'static str,
    operating_mode: &'static str,
}

#[tauri::command]
pub fn get_app_info() -> AppInfo {
    AppInfo {
        app_name: "Project Integrity OS",
        version: env!("CARGO_PKG_VERSION"),
        core_status: "ready",
        operating_mode: "deterministic-first",
    }
}
