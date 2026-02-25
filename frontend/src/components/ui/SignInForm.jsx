import React, { useId } from "react";
import { useIntl } from "react-intl";
import LabeledInput from "./LabeledInput";

export default function SignInForm({
  usernameOrEmail,
  onUsernameOrEmailChange = () => {},
  password,
  onPasswordChange = () => {},
  rememberMe,
  onRememberMeChange = () => {},
  onSubmit = () => {},
  onForgotPassword = () => {},
  onContinue = () => {},
  forgotPasswordHref,
}) {
  const intl = useIntl();
  const usernameId = useId();
  const passwordId = useId();

  return (
    <form
      className="flex w-full flex-col gap-4"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit({
          usernameOrEmail,
          password,
          rememberMe,
        });
        onContinue();
      }}
    >
      <LabeledInput
        id={usernameId}
        name="usernameOrEmail"
        label={intl.formatMessage({ id: "signInForm.usernameOrEmailLabel" })}
        value={usernameOrEmail}
        onChange={onUsernameOrEmailChange}
        placeholder={intl.formatMessage({ id: "signInForm.usernameOrEmailPlaceholder" })}
        autoComplete="username"
        inputMode="email"
        type="text"
      />

      <LabeledInput
        id={passwordId}
        name="password"
        label={intl.formatMessage({ id: "signInForm.passwordLabel" })}
        value={password}
        onChange={onPasswordChange}
        placeholder={intl.formatMessage({ id: "signInForm.passwordPlaceholder" })}
        autoComplete="current-password"
        type="password"
      />

      <div className="flex items-center justify-between">
        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={rememberMe}
            onChange={(e) => onRememberMeChange(e.target.checked)}
            className="h-[13px] w-[13px] rounded-[3px] border border-[#cbd5e1] bg-white text-[#155dfc] focus:outline-none focus:ring-2 focus:ring-[#155dfc]/20"
            aria-label="Remember me"
          />
          <span className="text-[16px] font-medium leading-6 tracking-[-0.3125px] text-[#4a5565]">
            {intl.formatMessage({ id: "signInForm.rememberMe" })}
          </span>
        </label>

        <a
          href={forgotPasswordHref || "#"}
          onClick={(e) => {
            if (!forgotPasswordHref) e.preventDefault();
            onForgotPassword();
          }}
          className="text-[14px] font-normal leading-5 tracking-[-0.1504px] text-[#155dfc] hover:underline focus:outline-none focus:ring-2 focus:ring-[#155dfc]/20"
        >
          {intl.formatMessage({ id: "common.forgotPassword" })}
        </a>
      </div>

      <button
        type="submit"
        onClick={() => onContinue()}
        className="h-11 w-full rounded-lg bg-[#030213] text-center text-[14px] font-medium leading-5 tracking-[-0.1504px] text-white shadow-sm transition-colors hover:bg-[#0b0b14] focus:outline-none focus:ring-2 focus:ring-[#155dfc]/25 active:opacity-95"
      >
        {intl.formatMessage({ id: "common.continue" })}
      </button>
    </form>
  );
}