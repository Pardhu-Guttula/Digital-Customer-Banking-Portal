import React, { useState } from "react";
import { useIntl } from "react-intl";
import AuthShell from "./layout/AuthShell";
import BrandHeader from "./layout/BrandHeader";
import SecurityCaption from "./layout/SecurityCaption";
import SignInCard from "./ui/SignInCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/227f9705-cf43-40cd-ae14-1f5942ae9581";
const imgIcon1 = "https://www.figma.com/api/mcp/asset/8eb86048-daa9-4639-9340-289481bbd4cb";

export default function BankingSelfServicePortalDesign({
  title,
  subtitle,
  securityText,

  usernameValue: usernameValueProp,
  onUsernameChange = () => {},
  passwordValue: passwordValueProp,
  onPasswordChange = () => {},
  rememberMeChecked: rememberMeCheckedProp,
  onRememberMeChange = () => {},

  onForgotPassword = () => {},
  onSubmit = () => {},

  loading = false,
  error = "",

  useRemoteBrandIcon = false,
  useRemoteUserIcon = false,
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.title" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.subtitle" });
  const resolvedSecurityText =
    securityText ?? intl.formatMessage({ id: "bankingSelfServicePortalDesign.securityText" });

  const [usernameValueState, setUsernameValueState] = useState("john.doe@email.com");
  const [passwordValueState, setPasswordValueState] = useState("");
  const [rememberMeCheckedState, setRememberMeCheckedState] = useState(false);

  const usernameValue = usernameValueProp !== undefined ? usernameValueProp : usernameValueState;
  const passwordValue = passwordValueProp !== undefined ? passwordValueProp : passwordValueState;
  const rememberMeChecked =
    rememberMeCheckedProp !== undefined ? rememberMeCheckedProp : rememberMeCheckedState;

  return (
    <AuthShell>
      <div className="w-full max-w-[448px] flex flex-col gap-6 items-stretch">
        <BrandHeader
          title={resolvedTitle}
          subtitle={resolvedSubtitle}
          useRemoteIcon={useRemoteBrandIcon}
          remoteIconSrc={imgIcon}
        />

        <SignInCard
          usernameValue={usernameValue}
          onUsernameChange={(next) => {
            if (usernameValueProp === undefined) setUsernameValueState(next);
            onUsernameChange(next);
          }}
          passwordValue={passwordValue}
          onPasswordChange={(next) => {
            if (passwordValueProp === undefined) setPasswordValueState(next);
            onPasswordChange(next);
          }}
          rememberMeChecked={rememberMeChecked}
          onRememberMeChange={(next) => {
            if (rememberMeCheckedProp === undefined) setRememberMeCheckedState(next);
            onRememberMeChange(next);
          }}
          onForgotPassword={onForgotPassword}
          onSubmit={onSubmit}
          loading={loading}
          error={error}
          useRemoteUserIcon={useRemoteUserIcon}
          remoteUserIconSrc={imgIcon1}
        />

        <SecurityCaption text={resolvedSecurityText} />
      </div>
    </AuthShell>
  );
}