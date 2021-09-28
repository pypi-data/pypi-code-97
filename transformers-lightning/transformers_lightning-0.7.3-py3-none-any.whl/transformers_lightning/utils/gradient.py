from torch.autograd import Function


class RevGrad(Function):
    r"""
    Copyright of this piece of code goes to https://github.com/janfreyberg/pytorch-revgrad

    Reverse the gradient values (* -1) while doing backpropagation.
    """

    @staticmethod
    def forward(ctx, input_):
        ctx.save_for_backward(input_)
        output = input_
        return output

    @staticmethod
    def backward(ctx, grad_output):    # pragma: no cover
        grad_input = None
        if ctx.needs_input_grad[0]:
            grad_input = -grad_output
        return grad_input


revgrad = RevGrad.apply
