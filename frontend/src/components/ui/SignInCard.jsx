import React, { useId } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import TextField from "./TextField";
import CheckboxField from "./CheckboxField";
import TextLink from "./TextLink";
import PrimaryButton from "./PrimaryButton";

export default function SignInCard({
  usernameOrEmail,
  password,
  rememberMe,
  loading = false,
  error = "",
  onUsernameOrEmailChange = () => {},
  onPasswordChange = () => {},
  onRememberMeChange = () => {},
  onForgotPassword = () => {},
  onSubmit = () => {},
}) {
  const intl = useIntl();

  const usernameId = useId();
  const passwordId = useId();

  return (
    <section
      aria-label="Sign in"
      className="w-full rounded-[14px] border border-[#E5E7EB] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="px-6 pt-6">
        <div className="flex items-center gap-2">
          <User className="h-5 w-5 text-[#0A0A0A]" aria-hidden="true" />
          <h2 className="text-[16px] font-medium leading-4 tracking-[-0.3125px] text-[#0A0A0A]">
            {intl.formatMessage({ id: "signInCard.title" })}
          </h2>
        </div>
        <p className="mt-2 text-[16px] leading-6 tracking-[-0.3125px] text-[#717182]">
          {intl.formatMessage({ id: "signInCard.description" })}
        </p>
      </div>

      <form
        className="flex w-full flex-col gap-4 px-6 pb-6 pt-6"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({
            usernameOrEmail,
            password,
            rememberMe,
          });
        }}
      >
        <TextField
          id={usernameId}
          label={intl.formatMessage({ id: "signInCard.usernameOrEmailLabel" })}
          type="text"
          value={usernameOrEmail}
          placeholder={intl.formatMessage({
            id: "signInCard.usernameOrEmailPlaceholder",
          })}
          autoComplete="username"
          onChange={onUsernameOrEmailChange}
        />

        <TextField
          id={passwordId}
          label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
          type="password"
          value={password}
          placeholder={intl.formatMessage({
            id: "signInCard.passwordPlaceholder",
          })}
          autoComplete="current-password"
          onChange={onPasswordChange}
        />

        <div className="flex w-full items-center justify-between gap-3">
          <CheckboxField
            checked={rememberMe}
            label={intl.formatMessage({ id: "signInCard.rememberMe" })}
            onChange={onRememberMeChange}
          />
          <TextLink
            label={intl.formatMessage({ id: "signInCard.forgotPassword" })}
            onClick={onForgotPassword}
          />
        </div>

        {error ? (
          <p className="text-sm text-red-600" role="alert">
            {error}
          </p>
        ) : null}

        <PrimaryButton
          label={
            loading
              ? intl.formatMessage({ id: "common.continuing" })
              : intl.formatMessage({ id: "common.continue" })
          }
          disabled={loading}
        />
      </form>
    </section>
  );
}