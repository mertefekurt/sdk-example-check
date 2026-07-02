from __future__ import annotations

from sdk_example_check.models import Rule

PROJECT_NAME = 'sdk-example-check'
SUMMARY = 'Audit SDK examples for hardcoded keys, missing errors, and outdated imports.'
SAMPLE_RISK = 'api_key sk_live_123 error handling missing old_import true'
SAMPLE_CLEAN = 'api_key env MY_API_KEY try except current_import true'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='hardcoded-key',
        severity='high',
        pattern='sk_live_|(?<![A-Za-z0-9_])api_key\\s+(?!env\\b)[A-Za-z0-9_]+',
        message='API key appears hardcoded',
        recommendation='load credentials from environment',
    ),
    Rule(
        code='missing-errors',
        severity='medium',
        pattern='error handling\\s+missing',
        message='error handling is missing',
        recommendation='show exception handling',
    ),
    Rule(
        code='old-import',
        severity='low',
        pattern='old_import\\s+true',
        message='outdated import noted',
        recommendation='update SDK import path',
    ),
)
