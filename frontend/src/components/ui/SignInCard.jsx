import React, { useId } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import LabeledInput from "./LabeledInput";
import RememberMeRow from "./RememberMeRow";
import PrimaryButton from "./PrimaryButton";

function noop() {}

export default function SignInCard({
  title,
  helperText,
  username,
  password,
  rememberMe,
  onUsernameChange = noop,
  onPasswordChange = noop,
  onRememberMeChange = noop,
  onForgotPassword = noop,
  onSubmit = noop,
  onContinueClick = noop,
  loading = false,
  error = "",
  useRemoteHeaderIcon = false,
  forgotHref,
  imgIcon1,
}) {
  const intl = useIntl();

  const usernameId = useId();
  const passwordId = useId();

  const resolvedTitle = title ?? intl.formatMessage({ id: "signInCard.title" });
  const resolvedHelperText =
    helperText ?? intl.formatMessage({ id: "signInCard.helperText" });

  return (
    <section
      aria-label="Sign in"
      className="w-full rounded-[14px] border border-[#e5e7eb] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="flex flex-col gap-1 px-6 pt-6">
        <div className="flex items-center gap-[6px]">
          {useRemoteHeaderIcon ? (
            <img src={imgIcon1} alt="" className="h-5 w-5" />
          ) : (
            <User className="h-5 w-5 text-[#0a0a0a]" aria-hidden="true" />
          )}
          <h2 className="text-[16px] font-medium leading-4 tracking-[-0.3125px] text-[#0a0a0a]">
            {resolvedTitle}
          </h2>
        </div>

        <p className="text-[16px] font-normal leading-6 tracking-[-0.3125px] text-[#717182]">
          {resolvedHelperText}
        </p>
      </div>

      <form
        className="flex w-full flex-col gap-4 px-6 pb-6 pt-4"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({ username, password, rememberMe });
        }}
      >
        <LabeledInput
          id={usernameId}
          name="username"
          label={intl.formatMessage({ id: "signInCard.usernameLabel" })}
          type="text"
          value={username}
          placeholder={intl.formatMessage({ id: "signInCard.usernamePlaceholder" })}
          onChange={onUsernameChange}
          autoComplete="username"
          inputMode="email"
        />

        <LabeledInput
          id={passwordId}
          name="password"
          label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
          type="password"
          value={password}
          placeholder={intl.formatMessage({ id: "signInCard.passwordPlaceholder" })}
          onChange={onPasswordChange}
          autoComplete="current-password"
        />

        <RememberMeRow
          checked={rememberMe}
          onCheckedChange={onRememberMeChange}
          onForgotPassword={onForgotPassword}
          forgotHref={forgotHref}
        />

        {error ? (
          <p className="text-[13px] leading-5 text-red-600" role="alert">
            {error}
          </p>
        ) : null}

        <PrimaryButton
          loading={loading}
          disabled={!username || !password}
          type="submit"
          onClick={() => onContinueClick({ username, password, rememberMe })}
        >
          {intl.formatMessage({ id: "signInCard.continue" })}
        </PrimaryButton>
      </form>
    </section>
  );
}