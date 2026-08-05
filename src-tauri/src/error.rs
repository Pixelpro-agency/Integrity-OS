use serde::Serialize;
use std::collections::BTreeMap;
use std::fmt;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum AppErrorCode {
    ApplicationStartupFailed,
    LoggingInitializationFailed,
}

impl AppErrorCode {
    pub const fn as_str(self) -> &'static str {
        match self {
            Self::ApplicationStartupFailed => "APPLICATION_STARTUP_FAILED",
            Self::LoggingInitializationFailed => "LOGGING_INITIALIZATION_FAILED",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct AppError {
    code: AppErrorCode,
    message: String,
    context: Option<BTreeMap<String, String>>,
}

impl AppError {
    pub fn new(code: AppErrorCode, message: impl Into<String>) -> Self {
        Self {
            code,
            message: message.into(),
            context: None,
        }
    }

    pub fn application_startup_failed() -> Self {
        Self::new(
            AppErrorCode::ApplicationStartupFailed,
            "The application could not start.",
        )
        .with_context("component", "tauri_runtime")
    }

    pub fn logging_initialization_failed() -> Self {
        Self::new(
            AppErrorCode::LoggingInitializationFailed,
            "Application logging could not be initialized.",
        )
        .with_context("component", "tracing_subscriber")
    }

    pub fn with_context(mut self, key: impl Into<String>, value: impl Into<String>) -> Self {
        self.context
            .get_or_insert_with(BTreeMap::new)
            .insert(key.into(), value.into());

        self
    }

    pub const fn code(&self) -> AppErrorCode {
        self.code
    }

    pub fn message(&self) -> &str {
        &self.message
    }
}

impl fmt::Display for AppError {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(formatter, "{}: {}", self.code.as_str(), self.message())
    }
}

impl std::error::Error for AppError {}

#[cfg(test)]
mod tests {
    use super::{AppError, AppErrorCode};
    use serde_json::json;

    #[test]
    fn app_error_serializes_the_frontend_contract() {
        let without_context = AppError::new(
            AppErrorCode::ApplicationStartupFailed,
            "A safe public message.",
        );

        let with_context = AppError::application_startup_failed();

        assert_eq!(
            serde_json::to_value(without_context)
                .expect("AppError without context should be serializable"),
            json!({
                "code": "APPLICATION_STARTUP_FAILED",
                "message": "A safe public message.",
                "context": null,
            })
        );

        assert_eq!(
            serde_json::to_value(with_context)
                .expect("AppError with context should be serializable"),
            json!({
                "code": "APPLICATION_STARTUP_FAILED",
                "message": "The application could not start.",
                "context": {
                    "component": "tauri_runtime",
                },
            })
        );
    }
}
