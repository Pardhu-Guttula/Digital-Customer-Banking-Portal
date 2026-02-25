import React, { useId, useMemo } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import Card from "./Card";
import LabeledInput from "./LabeledInput";
import CheckboxField from "./CheckboxField";
import TextLink from "./TextLink";
import PrimaryButton from "./PrimaryButton";

export default function SignInCard({
  usernameValue,
  onUsernameChange = () => {},
  passwordValue,
  onPasswordChange = () => {},
  rememberMeChecked,
  onRememberMeChange = () => {},
  onForgotPassword = () => {},
  onSubmit = () => {},
  loading = false,
  error = "",
  useRemoteUserIcon = false,
  remoteUserIconSrc,
}) {
  const intl = useIntl();

  const usernameId = useId();
  const passwordId = useId();

  const canSubmit = useMemo(() => {
    return Boolean(usernameValue && passwordValue) && !loading;
  }, [usernameValue, passwordValue, loading]);

  return (
    <Card className="w-full">
      <div className="px-6 pt-6">
        <div className="flex items-center gap-[6px]">
          <div className="h-5 w-5">
            {useRemoteUserIcon ? (
              <img src={remoteUserIconSrc} alt="" className="h-5 w-5" />
            ) : (
              <User className="h-5 w-5 text-[#0a0a0a]" aria-hidden="true" />
            )}
          </div>
          <h2 className="text-[16px] leading-4 font-medium text-[#0a0a0a] tracking-[-0.3125px]">
            {intl.formatMessage({ id: "signInCard.title" })}
          </h2>
        </div>

        <p className="mt-[6px] text-[16px] leading-6 text-[#717182] tracking-[-0.3125px]">
          {intl.formatMessage({ id: "signInCard.subtitle" })}
        </p>
      </div>

      <form
        className="px-6 pt-4 pb-6 flex flex-col gap-4"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({
            username: usernameValue,
            password: passwordValue,
            rememberMe: rememberMeChecked,
          });
        }}
      >
        <LabeledInput
          id={usernameId}
          label={intl.formatMessage({ id: "signInCard.usernameLabel" })}
          type="text"
          value={usernameValue}
          placeholder={intl.formatMessage({ id: "signInCard.usernamePlaceholder" })}
          autoComplete="username"
          inputMode="email"
          onChange={onUsernameChange}
        />

        <LabeledInput
          id={passwordId}
          label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
          type="password"
          value={passwordValue}
          placeholder={intl.formatMessage({ id: "signInCard.passwordPlaceholder" })}
          autoComplete="current-password"
          onChange={onPasswordChange}
        />

        <div className="flex items-center justify-between gap-4">
          <CheckboxField
            id="remember-me"
            checked={rememberMeChecked}
            onCheckedChange={onRememberMeChange}
            label={intl.formatMessage({ id: "signInCard.rememberMe" })}
          />

          <TextLink onClick={onForgotPassword} href="#">
            {intl.formatMessage({ id: "signInCard.forgotPassword" })}
          </TextLink>
        </div>

        {error ? (
          <p className="text-[14px] leading-5 text-red-600" role="alert">
            {error}
          </p>
        ) : null}

        <PrimaryButton disabled={!canSubmit} loading={loading}>
          {intl.formatMessage({ id: "signInCard.continue" })}
        </PrimaryButton>
      </form>
    </Card>
  );
}