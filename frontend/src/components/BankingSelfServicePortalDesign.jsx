import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import BrandHeader from "./layout/BrandHeader";
import SecurityNote from "./layout/SecurityNote";
import SignInCard from "./ui/SignInCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/b1febb15-78c6-44e2-80ba-3ce5edd2b922";
const imgIcon1 = "https://www.figma.com/api/mcp/asset/ea22b803-388a-4156-8862-7d96d7fab9ef";

export default function BankingSelfServicePortalDesign({
  initialUsernameOrEmail = "john.doe@email.com",
  initialPassword = "",
  initialRememberMe = false,
  onSubmit = () => {},
  onForgotPassword = () => {},
  onBrandClick = () => {},
  forgotPasswordHref = "#",
  loading = false,
}) {
  const intl = useIntl();

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
    <main className="min-h-screen w-full" style={backgroundStyle}>
      <section className="min-h-screen w-full flex items-center justify-center px-4 py-10">
        <div className="w-full max-w-[448px] flex flex-col gap-6">
          <BrandHeader
            title={intl.formatMessage({ id: "brandHeader.title" })}
            subtitle={intl.formatMessage({ id: "brandHeader.subtitle" })}
            onBrandClick={onBrandClick}
          />

          <SignInCard
            usernameOrEmail={usernameOrEmail}
            password={password}
            rememberMe={rememberMe}
            onUsernameOrEmailChange={setUsernameOrEmail}
            onPasswordChange={setPassword}
            onRememberMeChange={setRememberMe}
            onForgotPassword={onForgotPassword}
            forgotPasswordHref={forgotPasswordHref}
            loading={loading}
            onSubmit={(payload) => onSubmit(payload)}
            headerIcon={User}
          />

          <SecurityNote text={intl.formatMessage({ id: "securityNote.text" })} />
        </div>
      </section>

      {/* Asset constants preserved from MCP output (not used directly after icon conversion) */}
      <img src={imgIcon} alt="" className="hidden" />
      <img src={imgIcon1} alt="" className="hidden" />
    </main>
  );
}