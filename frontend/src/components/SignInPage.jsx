import React, { useState } from "react";
import { useIntl } from "react-intl";
import AppIconBadge from "./layout/AppIconBadge";
import SignInCard from "./ui/SignInCard";
import SecurityNote from "./layout/SecurityNote";

const imgIcon = "https://www.figma.com/api/mcp/asset/053ff470-c643-4640-81c5-39b06ce41aa5";
const imgIcon1 = "https://www.figma.com/api/mcp/asset/b5d3e36a-d458-485d-b7f3-7fe01e3ee53e";

export default function SignInPage({
  initialValues = { usernameOrEmail: "john.doe@email.com", password: "", rememberMe: false },
  onSubmit = () => {},
  onForgotPassword = () => {},
  onRememberChange = () => {},
  loading = false,
  useRemoteBrandIcon = false,
  useRemoteHeaderIcon = false,
}) {
  const intl = useIntl();
  const [values, setValues] = useState(initialValues);

  return (
    <div className="min-h-screen w-full bg-white">
      <main className="flex min-h-screen w-full items-center justify-center bg-gradient-to-br from-[#EFF6FF] via-white to-[#EFF6FF] px-4 py-6">
        <div className="flex w-full max-w-[448px] flex-col items-stretch gap-6">
          <header className="flex flex-col items-center justify-center gap-2 text-center">
            <AppIconBadge useRemoteAsset={useRemoteBrandIcon} imgIcon={imgIcon} />
            <h1 className="m-0 text-[30px] font-bold leading-9 tracking-[0.3955px] text-[#101828]">
              {intl.formatMessage({ id: "signInPage.brandTitle" })}
            </h1>
            <p className="m-0 text-base font-normal leading-6 tracking-[-0.3125px] text-[#4A5565]">
              {intl.formatMessage({ id: "signInPage.brandSubtitle" })}
            </p>
          </header>

          <SignInCard
            values={values}
            onValuesChange={setValues}
            onSubmit={(payload) => onSubmit(payload)}
            onForgotPassword={onForgotPassword}
            onRememberChange={onRememberChange}
            loading={loading}
            useRemoteHeaderIcon={useRemoteHeaderIcon}
            imgIcon1={imgIcon1}
          />

          <SecurityNote text={intl.formatMessage({ id: "securityNote.text" })} />
        </div>
      </main>
    </div>
  );
}