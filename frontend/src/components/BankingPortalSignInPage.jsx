import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import BrandHeader from "./layout/BrandHeader";
import SecurityFootnote from "./layout/SecurityFootnote";
import SignInCard from "./ui/SignInCard";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/b8645a9a-da70-4ed5-8450-4ac7d1c30f1b";
const imgIcon1 =
  "https://www.figma.com/api/mcp/asset/bd356c35-b0bb-4149-8617-52a20139805f";

export default function BankingPortalSignInPage({
  title,
  subtitle,
  footnote,
  initialUsernameOrEmail,
  initialPassword,
  initialRemember,
  loading = false,
  error = "",
  onSubmit = () => {},
  onForgotPassword = () => {},
  onBrandClick = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "bankingPortalSignInPage.title" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "bankingPortalSignInPage.subtitle" });
  const resolvedFootnote =
    footnote ?? intl.formatMessage({ id: "bankingPortalSignInPage.footnote" });

  const [usernameOrEmail, setUsernameOrEmail] = useState(
    initialUsernameOrEmail ??
      intl.formatMessage({ id: "bankingPortalSignInPage.initialUsernameOrEmail" })
  );
  const [password, setPassword] = useState(initialPassword ?? "");
  const [remember, setRemember] = useState(initialRemember ?? false);

  const backgroundStyle = useMemo(
    () => ({
      backgroundImage:
        "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
    }),
    []
  );

  return (
    <main className="min-h-screen w-full" style={backgroundStyle}>
      <div className="flex min-h-screen w-full items-center justify-center px-4 py-10 sm:px-6">
        <div className="flex w-full max-w-[448px] flex-col items-stretch gap-6">
          <BrandHeader
            title={resolvedTitle}
            subtitle={resolvedSubtitle}
            onBrandClick={onBrandClick}
          />

          <SignInCard
            usernameOrEmail={usernameOrEmail}
            password={password}
            remember={remember}
            onUsernameOrEmailChange={setUsernameOrEmail}
            onPasswordChange={setPassword}
            onRememberChange={setRemember}
            onForgotPassword={onForgotPassword}
            onSubmit={onSubmit}
            loading={loading}
            error={error}
          />

          <SecurityFootnote text={resolvedFootnote} />
        </div>
      </div>

      {/* Preserved asset constants from Figma MCP (not used directly after icon conversion) */}
      <img src={imgIcon} alt="" className="hidden" />
      <img src={imgIcon1} alt="" className="hidden" />
    </main>
  );
}