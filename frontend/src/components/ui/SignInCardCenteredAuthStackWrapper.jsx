import React from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import TextField from "./TextField";

const imgIcon1 =
  "https://www.figma.com/api/mcp/asset/fa6688bc-dae6-47c5-9419-a00c26d98bc8";

export default function SignInCardCenteredAuthStackWrapper({
  username,
  password,
  rememberMe,
  onUsernameChange = () => {},
  onPasswordChange = () => {},
  onRememberMeChange = () => {},
  onForgotPassword = () => {},
  onContinue = () => {},
  loading = false,
  useRemoteUserIcon = false,
}) {
  const intl = useIntl();

  const headerIcon = useRemoteUserIcon ? (
    <img alt="" src={imgIcon1} style={styles.cardHeaderIconImg} />
  ) : (
    <User size={20} color="#0A0A0A" aria-hidden="true" />
  );

  return (
    <div
      style={styles.card}
      role="region"
      aria-label={intl.formatMessage({
        id: "signInCardCenteredAuthStackWrapper.regionAriaLabel",
      })}
    >
      <div style={styles.cardHeader}>
        <div style={styles.cardHeaderTitleRow}>
          <span style={styles.cardHeaderIconWrap}>{headerIcon}</span>
          <div style={styles.cardHeaderTitle}>
            {intl.formatMessage({
              id: "signInCardCenteredAuthStackWrapper.title",
            })}
          </div>
        </div>
        <div style={styles.cardHeaderDesc}>
          {intl.formatMessage({
            id: "signInCardCenteredAuthStackWrapper.description",
          })}
        </div>
      </div>

      <form
        style={styles.form}
        onSubmit={(e) => {
          e.preventDefault();
          onContinue({ username, password, rememberMe });
        }}
      >
        <TextField
          id="username"
          label={intl.formatMessage({
            id: "common.usernameOrEmail",
          })}
          value={username}
          placeholder={intl.formatMessage({
            id: "common.usernameEmailPlaceholder",
          })}
          onChange={onUsernameChange}
          autoComplete="username"
          styles={styles}
        />
        <TextField
          id="password"
          label={intl.formatMessage({
            id: "common.password",
          })}
          type="password"
          value={password}
          placeholder={intl.formatMessage({
            id: "common.passwordPlaceholder",
          })}
          onChange={onPasswordChange}
          autoComplete="current-password"
          styles={styles}
        />

        <div style={styles.utilityRow}>
          <label style={styles.rememberLabel}>
            <input
              type="checkbox"
              checked={rememberMe}
              onChange={(e) => onRememberMeChange(e.target.checked)}
              style={styles.checkbox}
            />
            <span style={styles.rememberText}>
              {intl.formatMessage({ id: "common.rememberMe" })}
            </span>
          </label>

          <button
            type="button"
            onClick={onForgotPassword}
            style={styles.forgotLink}
          >
            {intl.formatMessage({ id: "common.forgotPassword" })}
          </button>
        </div>

        <button
          type="submit"
          onClick={() => onContinue({ username, password, rememberMe })}
          disabled={loading}
          style={styles.primaryButton}
        >
          {loading
            ? intl.formatMessage({ id: "common.continuing" })
            : intl.formatMessage({ id: "common.continue" })}
        </button>
      </form>
    </div>
  );
}

const styles = {
  card: {
    background: "#FFFFFF",
    border: "1px solid #E5E7EB",
    borderRadius: 14,
    boxShadow: "0px 20px 25px rgba(0,0,0,0.10), 0px 8px 10px rgba(0,0,0,0.10)",
    overflow: "hidden",
  },

  cardHeader: {
    padding: 24,
    paddingBottom: 0,
    display: "flex",
    flexDirection: "column",
    gap: 6,
  },

  cardHeaderTitleRow: {
    display: "flex",
    alignItems: "center",
    gap: 8,
  },

  cardHeaderIconWrap: {
    width: 20,
    height: 20,
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    flex: "0 0 auto",
  },

  cardHeaderIconImg: {
    width: 20,
    height: 20,
    display: "block",
  },

  cardHeaderTitle: {
    color: "#0A0A0A",
    fontSize: 16,
    lineHeight: "16px",
    fontWeight: 500,
    letterSpacing: "-0.3125px",
  },

  cardHeaderDesc: {
    color: "#717182",
    fontSize: 16,
    lineHeight: "24px",
    fontWeight: 400,
    letterSpacing: "-0.3125px",
  },

  form: {
    padding: 24,
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
    color: "#0A0A0A",
    fontSize: 14,
    lineHeight: "14px",
    fontWeight: 500,
    letterSpacing: "-0.1504px",
  },

  input: {
    height: 44,
    borderRadius: 8,
    border: "1px solid rgba(0,0,0,0)",
    background: "#F3F3F5",
    padding: "4px 12px",
    fontSize: 14,
    color: "#111827",
    outline: "none",
    boxSizing: "border-box",
  },

  utilityRow: {
    height: 24,
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    gap: 12,
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
    cursor: "pointer",
  },

  rememberText: {
    color: "#4A5565",
    fontSize: 16,
    lineHeight: "24px",
    fontWeight: 500,
    letterSpacing: "-0.3125px",
  },

  forgotLink: {
    appearance: "none",
    border: "none",
    background: "transparent",
    padding: 0,
    cursor: "pointer",
    color: "#155DFC",
    fontSize: 14,
    lineHeight: "20px",
    fontWeight: 400,
    letterSpacing: "-0.1504px",
    textDecoration: "none",
  },

  primaryButton: {
    height: 44,
    borderRadius: 8,
    border: "1px solid rgba(0,0,0,0)",
    background: "#030213",
    color: "#FFFFFF",
    fontSize: 14,
    lineHeight: "20px",
    fontWeight: 500,
    letterSpacing: "-0.1504px",
    cursor: "pointer",
  },

  footnoteWrap: {
    display: "flex",
    justifyContent: "center",
  },

  footnote: {
    margin: 0,
    color: "#4A5565",
    fontSize: 14,
    lineHeight: "20px",
    fontWeight: 400,
    letterSpacing: "-0.1504px",
    textAlign: "center",
  },
};