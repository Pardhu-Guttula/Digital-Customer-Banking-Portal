import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import GlobalHeader from "./layout/GlobalHeader";
import GlobalFooter from "./layout/GlobalFooter";
import AuthCard from "./ui/AuthCard";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/d09f7d1c-a95c-4fda-9c9a-fe1e7ad4471a";
const imgIcon1 =
  "https://www.figma.com/api/mcp/asset/76a5fa9a-9ddf-4ee1-9c81-9e792abe417c";

function noop() {}

export default function BankingSelfServicePortalDesign({
  title,
  subtitle,
  securityText,

  usernameOrEmail: usernameOrEmailProp,
  onUsernameOrEmailChange = noop,
  password: passwordProp,
  onPasswordChange = noop,
  rememberMe: rememberMeProp,
  onRememberMeChange = noop,

  loading = false,

  onBrandClick = noop,
  onForgotPassword = noop,
  onContinue = noop,
  onSubmit = noop,
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ??
    intl.formatMessage({ id: "bankingSelfServicePortalDesign.title" });
  const resolvedSubtitle =
    subtitle ??
    intl.formatMessage({ id: "bankingSelfServicePortalDesign.subtitle" });
  const resolvedSecurityText =
    securityText ??
    intl.formatMessage({ id: "bankingSelfServicePortalDesign.securityText" });

  const isUsernameControlled = usernameOrEmailProp !== undefined;
  const isPasswordControlled = passwordProp !== undefined;
  const isRememberControlled = rememberMeProp !== undefined;

  const [usernameOrEmailUncontrolled, setUsernameOrEmailUncontrolled] = useState(
    intl.formatMessage({
      id: "bankingSelfServicePortalDesign.defaultUsernameOrEmail",
    })
  );
  const [passwordUncontrolled, setPasswordUncontrolled] = useState("");
  const [rememberMeUncontrolled, setRememberMeUncontrolled] = useState(false);

  const usernameOrEmail = isUsernameControlled
    ? usernameOrEmailProp
    : usernameOrEmailUncontrolled;

  const password = isPasswordControlled ? passwordProp : passwordUncontrolled;

  const rememberMe = isRememberControlled
    ? rememberMeProp
    : rememberMeUncontrolled;

  const handleUsernameChange = (next) => {
    if (!isUsernameControlled) setUsernameOrEmailUncontrolled(next);
    onUsernameOrEmailChange(next);
  };

  const handlePasswordChange = (next) => {
    if (!isPasswordControlled) setPasswordUncontrolled(next);
    onPasswordChange(next);
  };

  const handleRememberChange = (next) => {
    if (!isRememberControlled) setRememberMeUncontrolled(next);
    onRememberMeChange(next);
  };

  const backgroundStyle = useMemo(
    () => ({
      backgroundImage:
        "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
    }),
    []
  );

  return (
    <main className="min-h-screen w-full bg-white" style={backgroundStyle}>
      <section className="flex min-h-screen w-full items-center justify-center px-4 py-10">
        <div className="flex w-full max-w-[448px] flex-col items-stretch gap-6">
          <GlobalHeader
            title={resolvedTitle}
            subtitle={resolvedSubtitle}
            onBrandClick={onBrandClick}
          />

          <AuthCard
            title={intl.formatMessage({ id: "authCard.title" })}
            description={intl.formatMessage({ id: "authCard.description" })}
            usernameOrEmail={usernameOrEmail}
            onUsernameOrEmailChange={handleUsernameChange}
            password={password}
            onPasswordChange={handlePasswordChange}
            rememberMe={rememberMe}
            onRememberMeChange={handleRememberChange}
            onForgotPassword={onForgotPassword}
            onContinue={onContinue}
            onSubmit={onSubmit}
            loading={loading}
          />

          <GlobalFooter text={resolvedSecurityText} />
        </div>
      </section>

      {/* Preserved assets from MCP output (not used; icons are rendered via lucide-react) */}
      <img src={imgIcon} alt="" className="hidden" />
      <img src={imgIcon1} alt="" className="hidden" />
    </main>
  );
}