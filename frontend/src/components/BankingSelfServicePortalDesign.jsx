import React, { useState } from "react";
import { useIntl } from "react-intl";
import BrandHeader from "./layout/BrandHeader";
import SecurityFootnote from "./layout/SecurityFootnote";
import SignInCard from "./ui/SignInCard";

function noop() {}

export default function BankingSelfServicePortalDesign({
  usernameOrEmail: usernameOrEmailProp,
  password: passwordProp,
  rememberMe: rememberMeProp,
  onUsernameOrEmailChange = noop,
  onPasswordChange = noop,
  onRememberMeChange = noop,
  onForgotPassword = noop,
  onSubmit = noop,
  brandIconMode = "lucide",
  signInHeaderIconMode = "lucide",
}) {
  const intl = useIntl();

  const [usernameOrEmailLocal, setUsernameOrEmailLocal] = useState("john.doe@email.com");
  const [passwordLocal, setPasswordLocal] = useState("");
  const [rememberMeLocal, setRememberMeLocal] = useState(false);

  const isUsernameControlled = typeof usernameOrEmailProp === "string";
  const isPasswordControlled = typeof passwordProp === "string";
  const isRememberControlled = typeof rememberMeProp === "boolean";

  const usernameOrEmail = isUsernameControlled ? usernameOrEmailProp : usernameOrEmailLocal;
  const password = isPasswordControlled ? passwordProp : passwordLocal;
  const rememberMe = isRememberControlled ? rememberMeProp : rememberMeLocal;

  return (
    <main
      className="min-h-screen w-full bg-white"
      aria-label={intl.formatMessage({ id: "bankingPortal.mainAriaLabel" })}
      style={{
        backgroundImage:
          "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
      }}
    >
      <div className="flex min-h-screen w-full items-center justify-center px-4 py-10">
        <div className="flex w-full max-w-[448px] flex-col items-stretch gap-6">
          <BrandHeader iconMode={brandIconMode} />

          <SignInCard
            usernameOrEmail={usernameOrEmail}
            password={password}
            rememberMe={rememberMe}
            headerIconMode={signInHeaderIconMode}
            onUsernameOrEmailChange={(next) => {
              if (!isUsernameControlled) setUsernameOrEmailLocal(next);
              onUsernameOrEmailChange(next);
            }}
            onPasswordChange={(next) => {
              if (!isPasswordControlled) setPasswordLocal(next);
              onPasswordChange(next);
            }}
            onRememberMeChange={(next) => {
              if (!isRememberControlled) setRememberMeLocal(next);
              onRememberMeChange(next);
            }}
            onForgotPassword={onForgotPassword}
            onSubmit={onSubmit}
          />

          <SecurityFootnote />
        </div>
      </div>
    </main>
  );
}