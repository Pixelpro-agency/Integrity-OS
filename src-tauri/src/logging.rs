use crate::error::AppError;
use std::sync::OnceLock;
use tracing::Level;

static LOGGING_STATE: OnceLock<Result<(), AppError>> = OnceLock::new();

pub fn init() -> Result<(), AppError> {
    LOGGING_STATE
        .get_or_init(|| {
            let max_level = if cfg!(debug_assertions) {
                Level::DEBUG
            } else {
                Level::INFO
            };

            tracing_subscriber::fmt()
                .with_max_level(max_level)
                .with_target(false)
                .try_init()
                .map_err(|_| AppError::logging_initialization_failed())
        })
        .clone()
}
