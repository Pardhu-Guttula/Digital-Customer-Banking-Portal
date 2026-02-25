import React, { useId } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import FormField from "./FormField";
import RememberRow from "./RememberRow";
import PrimaryButton from "./PrimaryButton";

export default function SignInCard({
  usernameOrEmail,
  password,
  remember,
  onUsernameOrEmailChange = () => {},
  onPasswordChange = () => {},
  onRememberChange = () => {},
  onForgotPassword = () => {},
  onSubmit = () => {},
  loading = false,
  error = "",
}) {
  const intl = useIntl();
  const usernameId = useId();
  const passwordId = useId();

  return (
    <section
      aria-label="Sign in"
      className="w-full max-w-[448px] rounded-[14px] border border-[#e5e7eb] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="px-6 pt-6">
        <div className="flex items-center gap-[6px]">
          <User className="h-5 w-5 text-[#0a0a0a]" aria-hidden="true" />
          <h2 className="text-[16px] font-medium leading-4 tracking-[-0.3125px] text-[#0a0a0a]">
            {intl.formatMessage({ id: "signInCard.title" })}
          </h2>
        </div>
        <p className="mt-[6px] text-[16px] leading-6 tracking-[-0.3125px] text-[#717182]">
          {intl.formatMessage({ id: "signInCard.subtitle" })}
        </p>
      </div>

      <form
        className="flex flex-col gap-4 px-6 pb-6 pt-6"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({
            usernameOrEmail,
            password,
            remember,
          });
        }}
      >
        <FormField
          id={usernameId}
          label={intl.formatMessage({ id: "signInCard.usernameOrEmailLabel" })}
          name="usernameOrEmail"
          type="text"
          value={usernameOrEmail}
          placeholder={intl.formatMessage({
            id: "signInCard.usernameOrEmailPlaceholder",
          })}
          autoComplete="username"
          onChange={onUsernameOrEmailChange}
        />

        <FormField
          id={passwordId}
          label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
          name="password"
          type="password"
          value={password}
          placeholder={intl.formatMessage({ id: "signInCard.passwordPlaceholder" })}
          autoComplete="current-password"
          onChange={onPasswordChange}
        />

        <RememberRow
          remember={remember}
          onRememberChange={onRememberChange}
          onForgotPassword={onForgotPassword}
        />

        {error ? (
          <p className="text-[14px] leading-5 text-red-600" role="alert">
            {error}
          </p>
        ) : null}

        <PrimaryButton
          disabled={loading || !usernameOrEmail || !password}
          onClick={() => {}}
        >
          {loading
            ? intl.formatMessage({ id: "signInCard.continuing" })
            : intl.formatMessage({ id: "signInCard.continue" })}
        </PrimaryButton>
      </form>
    </section>
  );
}