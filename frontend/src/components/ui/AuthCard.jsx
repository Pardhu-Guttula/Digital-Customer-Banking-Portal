import React, { useId } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import TextField from "./TextField";
import RememberMeRow from "./RememberMeRow";
import PrimaryButton from "./PrimaryButton";

function noop() {}

export default function AuthCard({
  title,
  description,
  usernameOrEmail,
  onUsernameOrEmailChange = noop,
  password,
  onPasswordChange = noop,
  rememberMe,
  onRememberMeChange = noop,
  onForgotPassword = noop,
  onContinue = noop,
  onSubmit = noop,
  loading = false,
}) {
  const intl = useIntl();

  const usernameId = useId();
  const passwordId = useId();

  const resolvedTitle = title ?? intl.formatMessage({ id: "authCard.title" });
  const resolvedDescription =
    description ?? intl.formatMessage({ id: "authCard.description" });

  return (
    <section className="w-full rounded-[14px] border border-[#e5e7eb] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]">
      <div className="px-6 pt-6">
        <div className="flex items-center gap-2">
          <User className="h-5 w-5 text-[#0a0a0a]" aria-hidden="true" />
          <h2 className="text-base font-medium leading-4 tracking-[-0.3125px] text-[#0a0a0a]">
            {resolvedTitle}
          </h2>
        </div>

        <p className="mt-2 text-base leading-6 tracking-[-0.3125px] text-[#717182]">
          {resolvedDescription}
        </p>
      </div>

      <form
        className="flex w-full flex-col gap-4 px-6 pb-6 pt-4"
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
          label={intl.formatMessage({ id: "authCard.usernameOrEmailLabel" })}
          name="usernameOrEmail"
          type="text"
          value={usernameOrEmail}
          onChange={onUsernameOrEmailChange}
          placeholder={intl.formatMessage({
            id: "authCard.usernameOrEmailPlaceholder",
          })}
          autoComplete="username"
        />

        <TextField
          id={passwordId}
          label={intl.formatMessage({ id: "authCard.passwordLabel" })}
          name="password"
          type="password"
          value={password}
          onChange={onPasswordChange}
          placeholder={intl.formatMessage({ id: "authCard.passwordPlaceholder" })}
          autoComplete="current-password"
        />

        <RememberMeRow
          rememberMe={rememberMe}
          onRememberMeChange={onRememberMeChange}
          onForgotPassword={onForgotPassword}
        />

        <PrimaryButton
          disabled={loading}
          onClick={() => onContinue({ usernameOrEmail, password, rememberMe })}
        >
          {loading
            ? intl.formatMessage({ id: "authCard.continuing" })
            : intl.formatMessage({ id: "authCard.continue" })}
        </PrimaryButton>
      </form>
    </section>
  );
}