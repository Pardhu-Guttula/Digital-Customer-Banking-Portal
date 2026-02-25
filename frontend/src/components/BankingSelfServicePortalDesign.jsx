import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import BrandHeader from "./layout/BrandHeader";
import AuthCard from "./ui/AuthCard";
import SignInForm from "./ui/SignInForm";
import SecurityNote from "./layout/SecurityNote";

const imgIcon = "https://www.figma.com/api/mcp/asset/14dfab04-cdb8-4978-8859-c80805e75d69";
const imgIcon1 = "https://www.figma.com/api/mcp/asset/c6b15297-653f-455b-9283-5e6bbfe125e7";

export default function BankingSelfServicePortalDesign({
  title,
  subtitle,
  securityNote,
  onBrandClick = () => {},
  onForgotPassword = () => {},
  onSubmit = () => {},
  onContinue = () => {},
  forgotPasswordHref,
  initialUsernameOrEmail = "",
  initialPassword = "",
  initialRememberMe = false,
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.title" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.subtitle" });
  const resolvedSecurityNote =
    securityNote ??
    intl.formatMessage({ id: "bankingSelfServicePortalDesign.securityNote" });

  const [usernameOrEmail, setUsernameOrEmail] = useState(initialUsernameOrEmail);
  const [password, setPassword] = useState(initialPassword);
  const [rememberMe, setRememberMe] = useState(initialRememberMe);

  const backgroundStyle = useMemo(
    () => ({
      backgroundImage:
        "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
    }),
    []
  );

  return (
    <div className="min-h-screen w-full bg-white" style={backgroundStyle}>
      <main className="flex min-h-screen w-full items-center justify-center px-4 py-10 sm:px-6">
        <div className="flex w-full max-w-[448px] flex-col items-stretch gap-6">
          <BrandHeader
            title={resolvedTitle}
            subtitle={resolvedSubtitle}
            onBrandClick={onBrandClick}
          />

          <AuthCard
            title={intl.formatMessage({ id: "authCard.title" })}
            description={intl.formatMessage({ id: "authCard.description" })}
            onForgotPassword={onForgotPassword}
            forgotPasswordHref={forgotPasswordHref}
            forgotPasswordLabel={intl.formatMessage({ id: "common.forgotPassword" })}
          >
            <SignInForm
              usernameOrEmail={usernameOrEmail}
              onUsernameOrEmailChange={setUsernameOrEmail}
              password={password}
              onPasswordChange={setPassword}
              rememberMe={rememberMe}
              onRememberMeChange={setRememberMe}
              onForgotPassword={onForgotPassword}
              onSubmit={onSubmit}
              onContinue={onContinue}
              forgotPasswordHref={forgotPasswordHref}
            />
          </AuthCard>

          <SecurityNote text={resolvedSecurityNote} />
        </div>
      </main>

      {/* Asset constants preserved from input (not used directly after icon conversion) */}
      <img src={imgIcon} alt="" className="hidden" />
      <img src={imgIcon1} alt="" className="hidden" />
    </div>
  );
}