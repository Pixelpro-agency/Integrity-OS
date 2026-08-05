mod app;
mod error;
mod logging;

use error::AppError;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    match logging::init() {
        Ok(()) => tracing::debug!("Application logging initialized"),
        Err(error) => {
            tracing::warn!(
                code = error.code().as_str(),
                "Application logging initialization was not applied"
            );
            eprintln!("{error}");
        }
    }

    tracing::info!(application = "Project Integrity OS", "Starting application");

    if tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![app::get_app_info])
        .run(tauri::generate_context!())
        .is_err()
    {
        let error = AppError::application_startup_failed();

        tracing::error!(
            code = error.code().as_str(),
            component = "tauri_runtime",
            "Application startup failed"
        );

        eprintln!("{error}");
        std::process::exit(1);
    }
}
