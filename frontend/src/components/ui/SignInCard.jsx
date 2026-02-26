import React, { useId, useMemo, useState } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";

function Field({ id, label, type = "text", value, placeholder, onChange }) {
  return (
    <div style={stylesSignInCard.field}>
      <label htmlFor={id} style={stylesSignInCard.label}>
        {label}
      </label>
      <input
        id={id}
        type={type}
        value={value}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
        style={stylesSignInCard.input}
      />
    </div>
  );
}

function PrimaryButton({ children, disabled, onClick }) {
  return (
    <button
      type="submit"
      disabled={disabled}
      onClick={onClick}
      style={{
        ...stylesSignInCard.primaryButton,
        ...(disabled ? stylesSignInCard.primaryButtonDisabled : null),
      }}
    >
      {children}
    </button>
  );
}

export default function SignInCard({
  initialUsername = "john.doe@email.com",
  initialPassword = "••••••••",
  initialRememberMe = false,
  loading = false,
  error = "",
  onSubmit = () => {},
  onForgotPassword = () => {},
  onUsernameChange = () => {},
  onPasswordChange = () => {},
  onRememberMeChange = () => {},
  onContinueClick = () => {},
}) {
  const intl = useIntl();

  const uid = useId();
  const usernameId = `${uid}-username`;
  const passwordId = `${uid}-password`;

  const [username, setUsername] = useState(initialUsername);
  const [password, setPassword] = useState(initialPassword);
  const [rememberMe, setRememberMe] = useState(initialRememberMe);

  const canSubmit = useMemo(() => {
    if (loading) return false;
    return (
      String(username || "").trim().length > 0 &&
      String(password || "").trim().length > 0
    );
  }, [username, password, loading]);

  function handleSubmit(e) {
    e.preventDefault();
    const payload = { username, password, rememberMe };
    onContinueClick(payload);
    onSubmit(payload);
  }

  return (
    <section
      aria-label={intl.formatMessage({ id: "signInCard.sectionAriaLabel" })}
      style={stylesSignInCard.card}
    >
      <div style={stylesSignInCard.header}>
        <div style={stylesSignInCard.headerTitleRow}>
          <span aria-hidden="true" style={stylesSignInCard.headerIconWrap}>
            <User size={20} color="#0A0A0A" />
          </span>
          <h2 style={stylesSignInCard.headerTitle}>
            {intl.formatMessage({ id: "common.signIn" })}
          </h2>
        </div>
        <p style={stylesSignInCard.headerSubtitle}>
          {intl.formatMessage({ id: "common.signInDescription" })}
        </p>
      </div>

      <form onSubmit={handleSubmit} style={stylesSignInCard.form}>
        <Field
          id={usernameId}
          label={intl.formatMessage({ id: "common.usernameOrEmail" })}
          type="text"
          value={username}
          placeholder={intl.formatMessage({ id: "common.usernameEmailPlaceholder" })}
          onChange={(next) => {
            setUsername(next);
            onUsernameChange(next);
          }}
        />

        <Field
          id={passwordId}
          label={intl.formatMessage({ id: "common.password" })}
          type="password"
          value={password}
          placeholder={intl.formatMessage({ id: "common.passwordPlaceholder" })}
          onChange={(next) => {
            setPassword(next);
            onPasswordChange(next);
          }}
        />

        <div style={stylesSignInCard.utilityRow}>
          <label style={stylesSignInCard.rememberLabel}>
            <input
              type="checkbox"
              checked={rememberMe}
              onChange={(e) => {
                const next = e.target.checked;
                setRememberMe(next);
                onRememberMeChange(next);
                onRememberMeChange(next);
              }}
              style={stylesSignInCard.checkbox}
            />
            <span style={stylesSignInCard.rememberText}>
              {intl.formatMessage({ id: "common.rememberMe" })}
            </span>
          </label>

          <button
            type="button"
            onClick={onForgotPassword}
            style={stylesSignInCard.forgotLink}
            onMouseEnter={(e) => {
              e.currentTarget.style.textDecoration = "underline";
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.textDecoration = "none";
            }}
          >
            {intl.formatMessage({ id: "common.forgotPassword" })}
          </button>
        </div>

        {error ? <div style={stylesSignInCard.error}>{error}</div> : null}

        <PrimaryButton disabled={!canSubmit} onClick={() => {}}>
          {loading
            ? intl.formatMessage({ id: "common.continuing" })
            : intl.formatMessage({ id: "common.continue" })}
        </PrimaryButton>
      </form>
    </section>
  );
}

const stylesSignInCard = {
  card: {
    width: 448,
    backgroundColor: "#FFFFFF",
    border: "1px solid #E5E7EB",
    borderRadius: 14,
    boxShadow: "0px 20px 25px rgba(0,0,0,0.10), 0px 8px 10px rgba(0,0,0,0.10)",
    overflow: "hidden",
  },
  header: {
    padding: 24,
    paddingBottom: 0,
    display: "flex",
    flexDirection: "column",
    gap: 6,
  },
  headerTitleRow: {
    display: "flex",
    alignItems: "center",
    gap: 8,
  },
  headerIconWrap: {
    width: 20,
    height: 20,
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
  },
  headerTitle: {
    margin: 0,
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontWeight: 500,
    fontSize: 16,
    lineHeight: "16px",
    letterSpacing: "-0.3125px",
    color: "#0A0A0A",
  },
  headerSubtitle: {
    margin: 0,
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontWeight: 400,
    fontSize: 16,
    lineHeight: "24px",
    letterSpacing: "-0.3125px",
    color: "#717182",
  },
  form: {
    padding: 24,
    paddingTop: 16,
    display: "flex",
    flexDirection: "column",
    gap: 16,
  },
  field: {
    display: "flex",
    flexDirection: "column",
    gap: 8,
  },
  label: {
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontWeight: 500,
    fontSize: 14,
    lineHeight: "14px",
    letterSpacing: "-0.1504px",
    color: "#0A0A0A",
  },
  input: {
    height: 44,
    width: "100%",
    boxSizing: "border-box",
    borderRadius: 8,
    border: "1px solid rgba(0,0,0,0)",
    backgroundColor: "#F3F3F5",
    padding: "4px 12px",
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontWeight: 400,
    fontSize: 14,
    letterSpacing: "-0.1504px",
    color: "#111827",
    outline: "none",
  },
  utilityRow: {
    height: 24,
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
  },
  rememberLabel: {
    display: "inline-flex",
    alignItems: "center",
    gap: 8,
    cursor: "pointer",
    userSelect: "none",
  },
  checkbox: {
    width: 13,
    height: 13,
    margin: 0,
    accentColor: "#155DFC",
  },
  rememberText: {
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontWeight: 500,
    fontSize: 16,
    lineHeight: "24px",
    letterSpacing: "-0.3125px",
    color: "#4A5565",
  },
  forgotLink: {
    border: "none",
    background: "transparent",
    padding: 0,
    margin: 0,
    cursor: "pointer",
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontWeight: 400,
    fontSize: 14,
    lineHeight: "20px",
    letterSpacing: "-0.1504px",
    color: "#155DFC",
    textDecoration: "none",
  },
  error: {
    marginTop: -4,
    marginBottom: 4,
    padding: "10px 12px",
    borderRadius: 8,
    backgroundColor: "#FEF2F2",
    border: "1px solid #FECACA",
    color: "#991B1B",
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontSize: 14,
    lineHeight: "20px",
  },
  primaryButton: {
    height: 44,
    width: "100%",
    borderRadius: 8,
    border: "1px solid rgba(0,0,0,0)",
    backgroundColor: "#030213",
    color: "#FFFFFF",
    fontFamily:
      "Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    fontWeight: 500,
    fontSize: 14,
    lineHeight: "20px",
    letterSpacing: "-0.1504px",
    cursor: "pointer",
  },
  primaryButtonDisabled: {
    opacity: 0.6,
    cursor: "not-allowed",
  },
};