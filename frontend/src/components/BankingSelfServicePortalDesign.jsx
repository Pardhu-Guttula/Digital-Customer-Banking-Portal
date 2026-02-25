import React, { useState } from "react";
import { useIntl } from "react-intl";
import AuthLayout from "./layout/AuthLayout";
import BrandHeader from "./layout/BrandHeader";
import SecurityNote from "./layout/SecurityNote";
import SignInCard from "./ui/SignInCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/95f964c2-bdae-4883-802b-f16916c88315";
const imgIcon1 = "https://www.figma.com/api/mcp/asset/39389a2f-d6b8-4718-be4a-70c37a6870a9";

export default function BankingSelfServicePortalDesign({
  usernameOrEmail: usernameOrEmailProp,
  password: passwordProp,
  rememberMe: rememberMeProp,
  loading = false,
  onUsernameOrEmailChange = () => {},
  onPasswordChange = () => {},
  onRememberMeChange = () => {},
  onForgotPassword = () => {},
  onSubmit = () => {},
}) {
  const intl = useIntl();

  const isControlled =
    typeof usernameOrEmailProp === "string" &&
    typeof passwordProp === "string" &&
    typeof rememberMeProp === "boolean";

  const [usernameOrEmailLocal, setUsernameOrEmailLocal] = useState(
    intl.formatMessage({ id: "bankingSelfServicePortalDesign.defaultUsernameOrEmail" })
  );
  const [passwordLocal, setPasswordLocal] = useState("");
  const [rememberMeLocal, setRememberMeLocal] = useState(false);

  const usernameOrEmail = isControlled ? usernameOrEmailProp : usernameOrEmailLocal;
  const password = isControlled ? passwordProp : passwordLocal;
  const rememberMe = isControlled ? rememberMeProp : rememberMeLocal;

  const handleUsernameOrEmailChange = (next) => {
    if (!isControlled) setUsernameOrEmailLocal(next);
    onUsernameOrEmailChange(next);
  };

  const handlePasswordChange = (next) => {
    if (!isControlled) setPasswordLocal(next);
    onPasswordChange(next);
  };

  const handleRememberMeChange = (next) => {
    if (!isControlled) setRememberMeLocal(next);
    onRememberMeChange(next);
  };

  const handleSubmit = (payload) => {
    onSubmit(payload);
  };

  return (
    <AuthLayout>
      <div className="w-full max-w-[448px] flex flex-col items-stretch gap-6">
        <BrandHeader />

        <SignInCard
          usernameOrEmail={usernameOrEmail}
          password={password}
          rememberMe={rememberMe}
          loading={loading}
          onUsernameOrEmailChange={handleUsernameOrEmailChange}
          onPasswordChange={handlePasswordChange}
          onRememberMeChange={handleRememberMeChange}
          onForgotPassword={onForgotPassword}
          onSubmit={handleSubmit}
        />

        <SecurityNote />
      </div>
    </AuthLayout>
  );
}