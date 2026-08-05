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

#[cfg(test)]
mod tests {
    use super::get_app_info;
    use serde_json::json;

    #[test]
    fn get_app_info_returns_the_frontend_contract() {
        let serialized =
            serde_json::to_value(get_app_info()).expect("AppInfo should be serializable");

        assert_eq!(
            serialized,
            json!({
                "appName": "Project Integrity OS",
                "version": env!("CARGO_PKG_VERSION"),
                "coreStatus": "ready",
                "operatingMode": "deterministic-first",
            })
        );
    }
}
