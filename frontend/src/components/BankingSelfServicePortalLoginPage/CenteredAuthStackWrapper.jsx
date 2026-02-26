import React, { useId, useMemo, useState } from "react";
import { useIntl } from "react-intl";
import BrandHeader from "../layout/BrandHeader";
import SignInCardCenteredAuthStackWrapper from "../ui/SignInCardCenteredAuthStackWrapper";
import SecurityFootnoteCenteredAuthStackWrapper from "../ui/SecurityFootnoteCenteredAuthStackWrapper";

export default function CenteredAuthStackWrapper({
  title,
  subtitle,
  footnote,
  onBrandClick = () => {},
  onForgotPassword = () => {},
  onContinue = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ??
    intl.formatMessage({ id: "centeredAuthStackWrapper.defaultTitle" });
  const resolvedSubtitle =
    subtitle ??
    intl.formatMessage({ id: "centeredAuthStackWrapper.defaultSubtitle" });
  const resolvedFootnote =
    footnote ??
    intl.formatMessage({ id: "centeredAuthStackWrapper.defaultFootnote" });

  const usernameId = useId();
  const passwordId = useId();

  const [username, setUsername] = useState("john.doe@email.com");
  const [password, setPassword] = useState("••••••••");
  const [rememberMe, setRememberMe] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleContinue = async (payload) => {
    onContinue(payload);
    setLoading(true);
    try {
      await Promise.resolve();
    } finally {
      setLoading(false);
    }
  };

  const fieldIds = useMemo(
    () => ({
      username: `username-${usernameId}`,
      password: `password-${passwordId}`,
    }),
    [usernameId, passwordId]
  );

  return (
    <div style={styles.viewportCenter}>
      <div
        style={styles.stack}
        aria-label={intl.formatMessage({
          id: "centeredAuthStackWrapper.authenticationAriaLabel",
        })}
      >
        <BrandHeader
          title={resolvedTitle}
          subtitle={resolvedSubtitle}
          onBrandClick={onBrandClick}
        />

        <SignInCardCenteredAuthStackWrapper
          username={username}
          password={password}
          rememberMe={rememberMe}
          onUsernameChange={setUsername}
          onPasswordChange={setPassword}
          onRememberMeChange={setRememberMe}
          onForgotPassword={onForgotPassword}
          onContinue={handleContinue}
          loading={loading}
          fieldIds={fieldIds}
        />

        <SecurityFootnoteCenteredAuthStackWrapper text={resolvedFootnote} />
      </div>
    </div>
  );
}

const styles = {
  viewportCenter: {
    width: "100%",
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "24px 16px",
    boxSizing: "border-box",
  },

  stack: {
    width: "100%",
    maxWidth: 448,
    display: "flex",
    flexDirection: "column",
    alignItems: "stretch",
    gap: 24,
  },
};