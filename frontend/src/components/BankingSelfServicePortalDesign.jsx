import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import BrandHeader from "./layout/BrandHeader";
import SecurityFootnote from "./layout/SecurityFootnote";
import SignInCard from "./ui/SignInCard";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/e1c0a465-2eb4-421b-912c-5dcee448d5ee";
const imgIcon1 =
  "https://www.figma.com/api/mcp/asset/8f864b25-dcb6-4e1a-8819-a0267fd40421";

export default function BankingSelfServicePortalDesign({
  initialUsernameOrEmail = "john.doe@email.com",
  initialPassword = "",
  initialRememberMe = false,
  loading = false,
  error = "",
  onBrandClick = () => {},
  onForgotPassword = () => {},
  onSubmit = () => {},
}) {
  const intl = useIntl();

  const [usernameOrEmail, setUsernameOrEmail] = useState(initialUsernameOrEmail);
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
    <main className="min-h-screen w-full bg-white" style={bgStyle}>
      <section className="flex min-h-screen w-full items-center justify-center px-4 py-10 sm:px-6">
        <div className="flex w-full max-w-[448px] flex-col gap-6">
          <BrandHeader
            title={intl.formatMessage({
              id: "brandHeader.title",
            })}
            subtitle={intl.formatMessage({
              id: "brandHeader.subtitle",
            })}
            onBrandClick={onBrandClick}
          />

          <SignInCard
            usernameOrEmail={usernameOrEmail}
            password={password}
            rememberMe={rememberMe}
            loading={loading}
            error={error}
            onUsernameOrEmailChange={setUsernameOrEmail}
            onPasswordChange={setPassword}
            onRememberMeChange={setRememberMe}
            onForgotPassword={onForgotPassword}
            onSubmit={onSubmit}
          />

          <SecurityFootnote
            text={intl.formatMessage({
              id: "securityFootnote.text",
            })}
          />
        </div>
      </section>
    </main>
  );
}