import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import BrandHeader from "./layout/BrandHeader";
import SecurityNote from "./layout/SecurityNote";
import SignInCard from "./ui/SignInCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/692f02e8-e233-4980-b2e0-a9d279fe1d0c";
const imgIcon1 = "https://www.figma.com/api/mcp/asset/2ee77454-eab8-4240-8de5-d523185fdc78";

function noop() {}

export default function BankingSelfServicePortalDesign({
  title,
  subtitle,
  securityNote,
  initialUsername = "",
  initialPassword = "",
  initialRememberMe = false,
  onBrandClick = noop,
  onForgotPassword = noop,
  onSubmit = noop,
  onContinueClick = noop,
  forgotHref,
  loading = false,
  error = "",
  useRemoteBrandIcon = false,
  useRemoteHeaderIcon = false,
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.title" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.subtitle" });
  const resolvedSecurityNote =
    securityNote ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.securityNote" });

  const [username, setUsername] = useState(initialUsername);
  const [password, setPassword] = useState(initialPassword);
  const [rememberMe, setRememberMe] = useState(initialRememberMe);

  const bgStyle = useMemo(
    () => ({
      backgroundImage:
        "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
    }),
    []
  );

  return (
    <div className="min-h-screen w-full bg-white" style={bgStyle}>
      <main className="mx-auto flex min-h-screen w-full items-center justify-center px-4 py-10">
        <div className="flex w-full max-w-[448px] flex-col gap-6">
          <BrandHeader
            title={resolvedTitle}
            subtitle={resolvedSubtitle}
            onBrandClick={onBrandClick}
            useRemoteIcon={useRemoteBrandIcon}
            imgIcon={imgIcon}
          />

          <SignInCard
            username={username}
            password={password}
            rememberMe={rememberMe}
            onUsernameChange={setUsername}
            onPasswordChange={setPassword}
            onRememberMeChange={setRememberMe}
            onForgotPassword={onForgotPassword}
            onSubmit={onSubmit}
            onContinueClick={onContinueClick}
            loading={loading}
            error={error}
            useRemoteHeaderIcon={useRemoteHeaderIcon}
            forgotHref={forgotHref}
            imgIcon1={imgIcon1}
          />

          <SecurityNote text={resolvedSecurityNote} />
        </div>
      </main>
    </div>
  );
}